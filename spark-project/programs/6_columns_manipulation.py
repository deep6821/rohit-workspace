from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('practise').getOrCreate()
file_location = "dbfs:/FileStore/shared_uploads/rohit.pandey02@nagarro.com/sample.csv"
df = spark.read.csv(file_location, header=True)
print(df.show())

"""
1. Adding Column: Use 'withColumn' the method takes two parameters column name and 
   data to add a new column to the existing data.
   
df = df.withColumn('NewColumn', df['EXPERIENCE'] + 2)
print(df.show())

2. Update column: Use 'withColumnRenamed' which takes to parameters existing column 
   name and new column name to rename the existing column.
   
df = df.withColumnRenamed('Existing Column', New Column)
print(df.show())

3. Delete Column: Use drop the method which takes the column name and returns the data.

df = df.drop('SALARY')
print(df.show())
"""
