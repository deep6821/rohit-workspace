"""
Kafka Consumer Utility

This module provides functions for consuming messages from a Kafka topic.
"""
from pyspark.sql.functions import col, expr, from_json


def get_kafka_stream(spark, configs, schema):
    """
    Creates a Kafka stream from a given topic and schema using Spark's built-in Kafka Source.

    Args:
        spark (SparkSession): The SparkSession object.
        configs (dict): A dictionary containing Kafka configurations (brokers, topic, etc.).
        schema (StructType): The expected schema for the Kafka data.

    Returns:
        pyspark.sql.streaming.DataStreamReader: The Kafka stream as a Spark DataFrame.
    """
    kafka_stream_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", configs["bootstrap_servers"]) \
        .option("subscribe", configs["topic"]) \
        .option("kafka.security.protocol", configs["security_protocol"]) \
        .option("kafka.auto.offset.reset", configs["auto_offset_reset"]) \
        .option("kafka.group.id", configs["group_id"]) \
        .option("kafka.client.id", configs["client_id"]) \
        .option("kafka.auto.commit.interval.ms", configs["auto_commit_interval_ms"]) \
        .option("kafka.heartbeat.interval.ms", configs["heartbeat_interval_ms"]) \
        .option("kafka.session.timeout.ms", configs["session_timeout_ms"]) \
        .option("kafka.request.timeout.ms", configs["request_timeout_ms"]) \
        .option("kafka.fetch.min.bytes", configs["fetch_min_bytes"]) \
        .option("kafka.fetch.max.bytes", configs["fetch_max_bytes"]) \
        .option("kafka.max.partition.fetch.bytes", configs["max_partition_fetch_bytes"]) \
        .option("kafka.max.poll.records", configs["max_poll_records"]) \
        .load()

    kafka_json_df = kafka_stream_df.withColumn("value", expr("cast(value as string)"))
    kafka_streaming_df = kafka_json_df.withColumn("values_json", from_json(col("value"), schema)).selectExpr(
        "values_json.*")

    return kafka_streaming_df
