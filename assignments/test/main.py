import os
from dotenv import load_dotenv

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# Load environment variables from .env
load_dotenv()

# Access AWS credentials
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")


schema = StructType([
      StructField("employee_id", IntegerType(), True),
      StructField("name", StringType(), True),
      StructField("salary", DoubleType(), True),
      StructField("department", StringType(), True)
])
spark = SparkSession.builder \
    .appName("example") \
    .config("spark.hadoop.fs.s3a.access.key", access_key_id) \
    .config("spark.hadoop.fs.s3a.secret.key", secret_access_key) \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

# Read from S3
# csv_file = "s3a://your-bucket-name/path/to/file.csv"
csv_file = "data.csv"
df = spark.read.csv(csv_file, header=True, schema=schema)

# Perform operations on DataFrame
df.show()

# Stop Spark session
spark.stop()
