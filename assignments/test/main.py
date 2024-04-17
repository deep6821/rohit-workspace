import os
from dotenv import load_dotenv
from functools import reduce

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# Load environment variables from .env
load_dotenv()

# Access AWS credentials
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region_name = os.getenv("AWS_REGION_NAME")
local_directory = os.getenv("LOCAL_DIRECTORY")

schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("salary", DoubleType(), True),
    StructField("department", StringType(), True)
])

# spark = SparkSession.builder \
#     .appName("example") \
#     .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.2,com.amazonaws:aws-java-sdk:1.12.702") \
#     .config("spark.hadoop.fs.s3a.access.key", access_key_id) \
#     .config("spark.hadoop.fs.s3a.secret.key", secret_access_key) \
#     .config("spark.hadoop.fs.s3a.region", region_name) \
#     .config("spark.hadoop.fs.s3a.endpoint", "s3.us-east-1.amazonaws.com") \
#     .config("spark.hadoop.fs.s3a.path.style.access", "true") \
#     .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.EnvironmentVariableCredentialsProvider") \
#     .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
#     .getOrCreate()

## Read from S3
# csv_file = "s3a://rohit-test-aws-bucket/data.csv"
## Perform operations on DataFrame
# df.show()
## Stop Spark session
# spark.stop()

spark = SparkSession.builder.appName("example").getOrCreate()

df_list = []
input_data_dir = os.path.join(os.getcwd(), local_directory)
for file_name in os.listdir(input_data_dir):
    if file_name.endswith(".csv"):
        csv_file_path = os.path.join(input_data_dir, file_name)
        df = spark.read.csv(csv_file_path, header=True, schema=schema)
        df_list.append(df)

# Vertically concatenate all DataFrames in the list by name
df = reduce(DataFrame.unionByName, df_list)

# Perform operations on DataFrame
df.show()

# Stop Spark session
spark.stop()
