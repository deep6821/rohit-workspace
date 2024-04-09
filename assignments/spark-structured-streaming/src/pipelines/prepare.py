"""
This module provides functions for preprocessing data by reading Kafka stream data from an S3 bucket parquet file,
extracting recipes with 'beef' as an ingredient, calculating average cooking time duration per difficulty level,
and writing the result to S3 in CSV format.
"""
import logging
import os
from dotenv import load_dotenv
from pyspark.sql.functions import avg, col, concat_ws, explode, split, trim, when, udf
from pyspark.sql.types import IntegerType

from utility.spark_session import get_spark_session
from utility.schema import load_schema, validate_schema
from utility.utils import setup_logging, get_config_path, load_config, write_to_csv


# Define a udf to convert time strings to seconds
def time_to_seconds(time_str):
    """
    Converts a time string in ISO format to seconds.

    Args:
        time_str (str): Time string in ISO format.

    Returns:
        int: Time in seconds.

    Example:
        time_to_seconds('3H30M') -> 12600
    """
    if time_str:
        hours, minutes = 0, 0
        if "H" in time_str:
            hours, rest = time_str.split("H")
            hours = int(hours)
            if "M" in rest:
                minutes = int(rest.split("M")[0])
        elif "M" in time_str:
            minutes = int(time_str.split("M")[0])
        return hours * 3600 + minutes * 60

    return 0


def preprocess_data():
    """
     Preprocesses data by reading Kafka stream data from an S3 bucket parquet file, extracting recipes with 'beef'
     as an ingredient, calculating average cooking time duration per difficulty level, and writing the result to
     S3 in CSV format.

     Returns:
         None

     Raises:
         Any exception encountered during data preprocessing.
     """
    setup_logging()
    logging.info("Preprocessing data...")
    try:
        # Load environment variables from .env file
        load_dotenv()
        environment = os.getenv("ENVIRONMENT", "dev")

        # Create Spark session
        spark = get_spark_session()
        # Load configurations
        aws_conf = load_config(get_config_path(f"configs/{environment}/aws_config.yml"))
        output_schema = load_schema(get_config_path("schema/schemas.yml"), "output_schema")
        output_path = aws_conf["output_path"]
        parquet_file_path = aws_conf["processed_data_path"]

        # Read data from Parquet file
        processed_df = spark.read.parquet(parquet_file_path)
        processed_df = processed_df.na.drop()

        # Explode the ingredients column to convert it from string to array
        processed_df = processed_df.withColumn("ingredients", trim(col("ingredients")))
        processed_df = processed_df.withColumn("ingredients", explode(split(col("ingredients"), "\n")))

        # Filter rows containing "beef" (case-insensitive) in the ingredients column
        beef_recipes_df = processed_df.filter(col("ingredients").contains("beef") | col("ingredients").contains("Beef"))

        # Define a udf to remove "PT" from the time string
        remove_pt_udf = udf(lambda time_str: time_str.replace("PT", ""))

        # Apply the udf to create new columns with "PT" removed
        beef_recipes_df = beef_recipes_df.withColumn("cook_time_without_pt", remove_pt_udf(col("cookTime")))
        beef_recipes_df = beef_recipes_df.withColumn("prep_time_without_pt", remove_pt_udf(col("prepTime")))

        # Register the udf
        time_to_seconds_udf = udf(time_to_seconds, IntegerType())

        # Convert cookTime and prepTime to seconds
        beef_recipes_df = beef_recipes_df.withColumn("cook_time_seconds",
                                                     time_to_seconds_udf(col("cook_time_without_pt")))
        beef_recipes_df = beef_recipes_df.withColumn("prep_time_seconds",
                                                     time_to_seconds_udf(col("prep_time_without_pt")))

        # Calculate total cooking time in seconds
        beef_recipes_df = beef_recipes_df.withColumn(
            "total_cook_time_seconds",
            col("cook_time_seconds") + col("prep_time_seconds")
        )

        # Define difficulty level based on total_cook_time
        beef_recipes_df = beef_recipes_df.withColumn(
            "difficulty",
            when(col("total_cook_time_seconds") < 30 * 60, "easy")
            .when((col("total_cook_time_seconds") >= 30 * 60) & (col("total_cook_time_seconds") <= 60 * 60), "medium")
            .otherwise("hard")
        )

        # # Group by difficulty and calculate average cooking time
        # avg_cooking_time_df = beef_recipes_df.groupBy("difficulty").agg(
        #     avg("total_cook_time_seconds").alias("avg_total_cooking_time_seconds").cast(DoubleType())
        # )

        # Group by difficulty and calculate average cooking time
        avg_cooking_time_df = beef_recipes_df.groupBy("difficulty").agg(
            avg("total_cook_time_seconds").alias("avg_total_cooking_time_seconds")
        )

        # Convert average cooking time from seconds to HH:MM format
        avg_cooking_time_df = avg_cooking_time_df.withColumn(
            "hours",
            (col("avg_total_cooking_time_seconds") / 3600).cast("int")
        )

        avg_cooking_time_df = avg_cooking_time_df.withColumn(
            "minutes",
            ((col("avg_total_cooking_time_seconds") % 3600) / 60).cast("int")
        )

        avg_cooking_time_df = avg_cooking_time_df.withColumn(
            "avg_total_cooking_time",
            concat_ws(
                ":",
                col("hours").cast("string"),
                col("minutes").cast("string")
            )
        )

        # Select only the required columns
        avg_cooking_time_df = avg_cooking_time_df.select("difficulty", "avg_total_cooking_time")

        # Validate data against schema
        validated_average_cook_time_df = validate_schema(avg_cooking_time_df, output_schema)

        # Write the result to S3 in CSV format
        write_to_csv(validated_average_cook_time_df, output_path, output_schema=output_schema)

        logging.info("Data preprocessed successfully!")
    except Exception as e:
        logging.error("Error processing data: %s", e)
        raise
