from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('practise').getOrCreate()

file_location = "dbfs:/FileStore/shared_uploads/rohit.pandey02@nagarro.com/sample.csv"

df = spark.read.csv(file_location, header=True, inferSchema=True)

# CSV
df.write.csv('dataset.csv')

# JSON
df.write.save('dataset.json', format='json')

# Parquet
df.write.save('dataset.parquet', format='parquet')

# CSV
df.select(['Name', 'Departments']).write.csv('dataset.csv')

# JSON
df.select(['Name', 'Departments']).write.save('dataset.json', format='json')

# Parquet
df.select(['Name', 'Departments']).write.save('dataset.parquet', format='parquet')
