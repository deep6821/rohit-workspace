from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

"""
df = spark.read.format("file_type")
        .option("inferSchema", )
        .option("header", )
        .option("sep", )
        .schema(schema_df)
        .load(file_path)

Formats:
    CSV,PARQUET,ORC,JSON,AVRO

Options:
    header="true"
    sep=""
    inferSchema="true"

Path:
    single path   ==> load(path1)
    multiple path ==> load(path1, path2)
    folder        ==> load(folder_path)

Schema:
    define
    schema(schema_df)

"""
spark = SparkSession.builder.appName('practise').getOrCreate()
file_path = "dbfs:/FileStore/shared_uploads/input/sample.csv"
file_format = "csv"
# df = spark.read.format("csv").option("header", "true").load(file_path)
df = spark.read.format(file_format).option("header", "true").option("sep", ",").option("inferSchema", "true").load(file_path)
# display(df)
print(df.show())

"""
+-------+-----------------+----+----------+------+
|   Name|       Department| Age|Experience|Salary|
+-------+-----------------+----+----------+------+
|  Rohit|Software Engineer|  31|         7|100000|
|Adhyeta|Software Engineer|  26|         2|100000|
|Adhyeta|Big Data Engineer|  26|         1|120000|
|  Rohit|    Data Engineer|  31|         7|120000|
|  Parul|             null|  26|      null|  null|
|   null|             null|null|      null|150000|
+-------+-----------------+----+----------+------+
"""
print(df.count())  # It will give number of records: 6
print(df.printSchema())
"""
root
 |-- Name: string (nullable = true)
 |-- Department: string (nullable = true)
 |-- Age: integer (nullable = true)
 |-- Experience: integer (nullable = true)
 |-- Salary: integer (nullable = true)
"""


# Create Our Own Schema
schema_defined =StructType([
    StructField('Name', StringType(), True),
    StructField('Department', StringType(), True),
    StructField('Age', IntegerType(), True),
    StructField('Experience', IntegerType(), True),
    StructField('Salary', IntegerType(), True),
])
df1 = spark.read.format(file_format).schema(schema_defined).option("header", "true").option("sep", ",").load(file_path)
print(df1.show())
