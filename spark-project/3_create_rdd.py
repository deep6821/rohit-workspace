"""
What is RDD (Resilient Distributed Dataset)?
--------------------------------------------
RDD (Resilient Distributed Dataset) is a fundamental building block of PySpark which is fault-tolerant, immutable
distributed collections of objects. Each record in RDD is divided into logical partitions, which can be computed on
different nodes of the cluster.

In other words, RDDs are a collection of objects similar to list in Python, with the difference being RDD is computed
on several processes scattered across multiple physical servers also called nodes in a cluster while a Python collection
lives and process in just one process.

Additionally, RDDs provide data abstraction of partitioning and distribution of the data designed to run computations in
parallel on several nodes, while doing transformations on RDD we don’t have to worry about the parallelism as PySpark by
default provides.


---------------------
1. In-Memory Processing
PySpark loads the data from disk and process in memory and keeps the data in memory, this is the main difference between
PySpark and Mapreduce (I/O intensive). In between the transformations, we can also cache/persists the RDD in memory to
reuse the previous computations.


2. Immutability
PySpark RDD’s are immutable in nature meaning, once RDDs are created you cannot modify. When we apply transformations on
RDD, PySpark creates a new RDD and maintains the RDD Lineage.


3. Fault Tolerance
PySpark operates on fault-tolerant data stores on HDFS, S3 e.t.c hence any RDD operation fails, it automatically reloads
the data from other partitions. Also, When PySpark applications running on a cluster, PySpark task failures are
automatically recovered for a certain number of times (as per the configuration) and finish the application seamlessly.

4. Lazy Evolution
PySpark does not evaluate the RDD transformations as they appear/encountered by Driver instead it keeps the all
transformations as it encounters(DAG) and evaluates the all transformation when it sees the first RDD action.

5. Partitioning
When you create RDD from a data, It by default partitions the elements in a RDD. By default it partitions to the number
of cores available.

PySpark RDD Limitations:
------------------------
PySpark RDDs are not much suitable for applications that make updates to the state store such as storage systems for a
web application.

For these applications, it is more efficient to use systems that perform traditional update logging and data
checkpointing, such as databases. The goal of RDD is to provide an efficient programming model for batch analytics and
leave these asynchronous applications.

Creating RDD:
-------------
RDD’s are created primarily in two different ways,

1. parallelizing an existing collection
2. referencing a dataset in an external storage system (HDFS, S3 and many more).


"""

from pyspark.sql import SparkSession
# Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
print("Spark Session: ", spark_session, type(spark_session))

dataList = data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
parallelize(): SparkContext (sparkContext.parallelize()) you can create an RDD. This function loads the
               existing collection from your driver program into parallelizing RDD. This is a basic 
               method to create RDD and is used when you already have data in memory that is either
               loaded from a file or from a database. and it required all data to be present on the 
               driver program prior to """
# creating RDD.
rdd = spark.sparkContext.parallelize(dataList)
print("RDD: ", rdd, type(rdd))

# Create RDD using sparkContext.textFile(): Using this, we can read a text (.txt) file into RDD
# Create RDD from external Data source
rdd2 = spark.sparkContext.textFile("/path/textFile.txt")

# Create RDD using sparkContext.wholeTextFiles(): This function returns a PairRDD with the key being the
# file path and value being file content.
# Reads entire file into a RDD as single record.
rdd3 = spark.sparkContext.wholeTextFiles("/path/textFile.txt")

# Create empty RDD using sparkContext.emptyRDD: This method on sparkContext we can create an RDD with no data.
# This method creates an empty RDD with no partition
rdd4 = spark.sparkContext.emptyRDD

# Create empty RDD with partition
rdd5 = spark.sparkContext.parallelize([],10) #This creates 10 partitions

## When we use parallelize() or textFile() or wholeTextFiles() methods of SparkContxt to initiate RDD,
# it automatically splits the data into partitions based on resource availability. when you run it on a
# laptop it would create partitions as the same number of cores available on your system.

# getNumPartitions() – This a RDD function which returns a number of partitions our dataset split into.
print("initial partition count:"+str(rdd.getNumPartitions()))



