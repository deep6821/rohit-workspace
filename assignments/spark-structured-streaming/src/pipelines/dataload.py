"""
This module provides functions to process data from Kafka and write it to S3 in Parquet format.
"""
import logging
import os
from dotenv import load_dotenv
from pyspark.sql.functions import col, current_date, dayofmonth, lit, month, to_date, year

from utility.kafka_consumer import get_kafka_stream
from utility.schema import load_schema, validate_schema
from utility.spark_session import get_spark_session
from utility.utils import setup_logging, get_config_path, load_config, get_latest_processed_date, write_to_s3_stream


def process_data():
    """
     Process data from Kafka and write to S3 in Parquet format.

     This function performs the following steps:
     1. Sets up logging.
     2. Retrieves Spark session.
     3. Loads configurations from YAML files.
     4. Loads input schema from YAML file.
     5. Reads data from Kafka using the provided schema.
     6. Validates the data against the input schema.
     7. Adds an event date column to the DataFrame.
     8. Adds partition columns for year, month, and day.
     9. Retrieve the latest processed date from the partitioned S3 location, filter the DataFrame to only include new
     data that has arrived since the last run(Incremental Processing)
     10. Writes the processed data to S3 in Parquet format, partitioned by year, month, and day.

     Returns:
         None

     Raises:
         Any exception encountered during data processing.
     """
    setup_logging()
    logging.info("Processing data...")
    try:
        # Load environment variables from .env file
        load_dotenv()
        environment = os.getenv("ENVIRONMENT", "dev")

        # Create Spark session
        spark = get_spark_session()

        # Load configurations
        aws_conf = load_config(get_config_path(f"configs/{environment}/aws_config.yml"))
        os.environ["AWS_ACCESS_KEY"] = aws_conf["aws_access_key"]
        os.environ["AWS_SECRET_KEY"] = aws_conf["aws_secret_key"]
        os.environ["AWS_REGION"] = aws_conf["region"]
        kafka_conf = load_config(get_config_path(f"configs/{environment}/kafka_config.yml"))

        # Load input and output schemas
        input_schema = load_schema(get_config_path("schema/schemas.yml"), "input_schema")

        # # Read data from Kafka
        kafka_streaming_df = get_kafka_stream(spark, kafka_conf, input_schema)

        # Validate data against schema
        validated_df = validate_schema(kafka_streaming_df, input_schema)

        # Add event date column
        processed_df = validated_df.withColumn("event_date", to_date(lit(current_date())))

        # Add partition columns
        processed_df = processed_df.withColumn("year", year(col("event_date")))
        processed_df = processed_df.withColumn("month", month(col("event_date")))
        processed_df = processed_df.withColumn("day", dayofmonth(col("event_date")))

        # Get the latest processed date: this is used to only process new data that has arrived since the last run
        latest_processed_date = get_latest_processed_date(spark, aws_conf)

        # Write input data to S3 in Parquet format, partitioned by year, month, and day
        write_to_s3_stream(aws_conf, processed_df, partition_cols=["year", "month", "day"], mode="append", latest_processed_date=latest_processed_date)

        logging.info("Data processed successfully!")
    except Exception as e:
        logging.error("Error processing data: %s", e)

        raise
