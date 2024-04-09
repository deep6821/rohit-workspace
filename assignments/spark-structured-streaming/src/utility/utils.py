"""
Utility Functions

This module provides utility functions for logging, configuration loading, retrieving the latest processed date, and writing data to S3.
"""
from datetime import datetime
import logging
from logging import handlers
import os
from dotenv import load_dotenv
import yaml

from pyspark.sql.functions import col, max

# Load environment variables from .env file
load_dotenv()
environment = os.getenv("ENVIRONMENT", "dev")


def setup_logging(logging_config_file=f"configs/{environment}/logging_config.yml"):
    """
    Sets up logging configuration based on a YAML config file.

    This function reads a YAML config file at the specified path and configures Python logging
    according to the settings defined in the file.

    It supports basic configuration options like logging level, format, and a CloudWatch handler.

    Args:
        logging_config_file (str, optional): The path to the YAML config file for logging.
        Defaults to "configs/dev/logging_config.yml".

    Returns:
        None
    """
    config_path = get_config_path(logging_config_file)
    with open(config_path, "r", encoding="utf-8") as f:
        logging_config = yaml.safe_load(f)

    logging.basicConfig(
        level=logging_config.get("logging", {}).get("level", "INFO"),
        format=logging_config.get("logging", {}).get("format", "%(asctime)s - %(levelname)s - %(message)s"),
        datefmt=logging_config.get("logging", {}).get("datefmt", "%Y-%m-%d %H:%M:%S")
    )

    cloudwatch_handler_config = logging_config.get("logging", {}).get("handlers", {}).get("cloudwatch", {})
    if cloudwatch_handler_config:
        cloudwatch_logger = logging.getLogger("cloudwatch")
        cloudwatch_logger.setLevel(cloudwatch_handler_config.get("level", "INFO"))
        cloudwatch_handler = handlers.SysLogHandler(address=cloudwatch_handler_config.get("address"))
        cloudwatch_handler.setFormatter(
            logging.Formatter(
                cloudwatch_handler_config.get("format", "%(asctime)s - %(levelname)s - %(message)s"),
                cloudwatch_handler_config.get("datefmt", "%Y-%m-%d %H:%M:%S")
            )
        )
        cloudwatch_logger.addHandler(cloudwatch_handler)


def get_config_path(relative_path):
    """
    Construct the absolute path to a configuration file based on the current script's directory.

    Args:
        relative_path (str): The relative path to the configuration file from the project root directory.

    Returns:
        str: The absolute path to the configuration file.
    """
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the config file
    config_path = os.path.join(script_dir, '../../', relative_path)
    return config_path


def load_config(config_file):
    """
    Loads configuration from a YAML file.

    This function reads a YAML file and returns the parsed configuration as a dictionary.

    Args:
        config_file (str): The path to the YAML config file.

    Returns:
        dict: The parsed configuration dictionary.
    """
    with open(config_file, "r", encoding="utf-8") as file:
        configs = yaml.safe_load(file)
    return configs


def get_latest_processed_date(spark, aws_conf):
    """
    Retrieves the latest processed date from the partitioned S3 location.

    Args:
        spark (SparkSession): The Spark session.
        aws_conf (dict): The AWS configuration.

    Returns:
        datetime.date: The latest processed date.
    """
    try:
        # Read the latest partition from S3
        latest_partition_df = spark.read.parquet(aws_conf["processed_data_path"])
        latest_partition_date = latest_partition_df.select(
            max("year"), max("month"), max("day")
        ).first()

        # Convert the latest partition date to a datetime.date object
        latest_processed_date = datetime(
            latest_partition_date[0], latest_partition_date[1], latest_partition_date[2]
        ).date()

        return latest_processed_date
    except Exception as e:
        logging.error("Error retrieving latest processed date:", exc_info=e)
        return None


def write_to_s3_stream(aws_conf, processed_df, partition_cols=None, mode="append", latest_processed_date=None):
    """
    Writes a DataFrame to S3 in Parquet format (streaming) with year, month, day partitioning.

    Args:
        aws_conf (dict): The AWS configuration.
        processed_df (pyspark.sql.DataFrame): The DataFrame to be written.
        partition_cols (list, optional): A list of column names to partition by. Defaults to None.
        mode (str, optional): The write mode ('append', 'overwrite' etc.). Defaults to "append".
        latest_processed_date (datetime.date, optional): The latest processed date.

    Returns:
        None
    """
    try:
        if latest_processed_date:
            # Filter the DataFrame to only include new data
            processed_df = processed_df.where(col("event_date") > latest_processed_date)

        query = (processed_df.writeStream
                 .format("parquet")
                 .partitionBy(*partition_cols)
                 .option("path", aws_conf["processed_data_path"])
                 .option("checkpointLocation", aws_conf["checkpoint_location"])
                 .outputMode(mode).start()
                 )

        query.awaitTermination()
    except Exception as e:
        logging.error("Error writing data to S3 stream:", exc_info=e)
        raise


def write_to_csv(df, output_path, output_schema=None, mode="overwrite"):
    """
    Write DataFrame to CSV with specified options.

    Args:
        df (DataFrame): The DataFrame to be written.
        output_path (str): The output path for the CSV file.
        output_schema (StructType, optional): The schema of the output DataFrame.
        mode (str, optional): The write mode ('append', 'overwrite' etc.). Defaults to "overwrite".

    Returns:
        None
    """
    try:
        df.write.mode(mode).option("header", True).csv(output_path, schema=output_schema)
    except Exception as e:
        logging.error("Error writing data to CSV file:", exc_info=e)
        raise
