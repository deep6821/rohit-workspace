from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('practise').getOrCreate()
file_location = r"C:\office\rohit-workspace\spark-project\inputs\missing_values.csv"
df = spark.read.csv(file_location, header=True, inferSchema=True)
df.na.drop().show()
"""
+-------+----+----------+------+
|   NAME|AGE |EXPERIENCE|SALARY|
+-------+----+----------+------+
|  Rohit|  31|         7|100000|
|Adhyeta|  26|         2| 50000|
|   Deep|  30|         6| 90000|
|  Parul|  25|         1| 40000|
+-------+----+----------+------+
"""
df.na.drop(how="any").show()
df.na.drop(how="all").show()
df.na.drop(how="all", thresh=2).show()  # al-least two non null value
df.na.drop(how="all", subset=['EXPERIENCE']).show()  # al-least two non null value

df.na.fill("Fill miss value").show()
df.na.fill("Fill miss value", ['EXPERIENCE']).show()





