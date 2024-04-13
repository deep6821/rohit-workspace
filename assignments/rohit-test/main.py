from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType


spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

csv_file  = "data.csv"

# Define data
data = [
    (1, "John Doe", 50000, "Engineering"),
    (2, "Jane Smith", 60000, "Human Resources"),
    (3, "Michael Johnson", 70000, "Finance"),
    (4, "Emily Brown", 55000, "Engineering"),
    (5, "David Lee", 65000, "Marketing"),
    (6, "Sarah Clark", 75000, "Finance"),
    (7, "Alexander Garcia", 60000, "Human Resources"),
    (8, "Emma Martinez", 52000, "Engineering"),
    (9, "James Anderson", 68000, "Marketing"),
    (10, "Sophia Taylor", 72000, "Finance")
]
# Define schema
schema = StructType([
      StructField("employee_id", IntegerType(), True),
      StructField("name", StringType(), True),
      StructField("salary", DoubleType(), True),
      StructField("department", StringType(), True)
])
# Create DataFrame
# df = spark.createDataFrame(data, schema)

df = spark.read.csv(csv_file, header=True, schema=schema)
print(df.show())
