spark = SparkSession.builder.appName('practise').getOrCreate()
file_path = "dbfs:/FileStore/shared_uploads/rohit.pandey02@nagarro.com/sample_zipcodes.csv"
file_format = "csv"
df = spark.read.format(file_format).option("header", "true").option("sep", ",").option("inferSchema", "true").load(file_path)
print(df.show())
