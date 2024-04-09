"""
Spark Session Utility

This module provides functions for creating a SparkSession using configurations from a YAML file.
"""
import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from utility.utils import get_config_path, load_config


def get_spark_session():
    """
    Creates a SparkSession using configurations from a YAML file.

    Args:
        None

    Returns:
        SparkSession: The SparkSession object.
    """
    # Load environment variables from .env file
    load_dotenv()
    environment = os.getenv("ENVIRONMENT", "dev")

    spark_conf = load_config(get_config_path(f"configs/{environment}/spark_config.yml"))
    return SparkSession.builder \
        .appName(spark_conf["app_name"]) \
        .config("spark.streaming.stopGracefullyOnShutdown", True) \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1") \
        .config("spark.executor.memory", spark_conf["executor_memory"]) \
        .config("spark.executor.cores", str(spark_conf["executor_cores"])) \
        .config("spark.cores.max", str(spark_conf["max_cores"])) \
        .config("spark.driver.memory", spark_conf["driver_memory"]) \
        .config("spark.sql.shuffle.partitions", str(spark_conf["shuffle_partitions"])) \
        .getOrCreate()
