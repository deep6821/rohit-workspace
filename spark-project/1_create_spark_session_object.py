import pyspark
from pyspark.sql import SparkSession

# Create SparkSession
spark_session = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
print("Spark Session: ", spark_session, type(spark_session))

"""
master() – If you are running it on the cluster you need to use your master name as an argument to master(). usually, it
would be either yarn or mesos depends on your cluster setup.

Use local[x] when running in Standalone mode. x should be an integer value and should be greater than 0; this represents
how many partitions it should create when using RDD, DataFrame, and Dataset. Ideally, x value should be the number of
CPU cores you have.

appName() – Used to set your application name.

getOrCreate() – This returns a SparkSession object if already exists, creates new one if not exists.

------------------------------------------------------------------------------------------------------------------------
You can also create a new SparkSession using newSession() method.
new_spark_session = SparkSession.newSession
"""