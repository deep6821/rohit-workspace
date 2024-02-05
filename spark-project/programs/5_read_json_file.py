from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType


spark = SparkSession.builder.appName('practise').getOrCreate()
file_path = "dbfs:/FileStore/shared_uploads/input/sample.json"
file_format = "json"
df = spark.read.format(file_format).option("multiline", "true").load(file_path)
print(df.show())

"""
+--------------------+
|              people|
+--------------------+
|[{28, Joe, male, ...|
+--------------------+
"""
