from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('practise').getOrCreate()
file_location = "dbfs:/FileStore/shared_uploads/rohit.pandey02@nagarro.com/sample.csv"
df = spark.read.csv(file_location, header=True)

"""
1. printSchema(): It displays the schema of the data

print(df.printSchema())
root
 |-- ID: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- AGE : string (nullable = true)
 |-- EXPERIENCE: string (nullable = true)
 |-- SALARY: string (nullable = true)
 
 2. head(n): It returns n rows as a list
 
print(df.head(2))

3. show(): It displays the first 20 rows by default and it also takes a number 
           as a parameter to display the number of rows of the data.
           
print(df.show())
print(df.show(2))
+---+-------+----+----------+------+
| ID|   NAME|AGE |EXPERIENCE|SALARY|
+---+-------+----+----------+------+
|  1|  Rohit|  31|         7|100000|
|  2|Adhyeta|  26|         2| 50000|
|  3|   Deep|  30|         6| 90000|
|  4|  Parul|  25|         1| 40000|
+---+-------+----+----------+------+

+---+-------+----+----------+------+
| ID|   NAME|AGE |EXPERIENCE|SALARY|
+---+-------+----+----------+------+
|  1|  Rohit|  31|         7|100000|
|  2|Adhyeta|  26|         2| 50000|

4. first(): It returns the first row of the data.

print(df.first())

5. take(n): It returns the first n rows of the data.

file_location = "dbfs:/FileStore/shared_uploads/rohit.pandey02@nagarro.com/querying_data.csv"

6. It computes the summary statistics of the columns with the numeric data type.

print(df.describe())
DataFrame[summary: string, ID: string, NAME: string, AGE : string, EXPERIENCE: string, SALARY: string]

print(df.describe().show())
+-------+-------+-----------------+------------------+
|summary|   Name|      Departments|            Salary|
+-------+-------+-----------------+------------------+
|  count|      5|                5|                 5|
|   mean|   null|             null|           82000.0|
| stddev|   null|             null|13038.404810405298|
|    min|Adhyeta|         Big Data|             70000|
|    max|  Rohit|Software Engineer|            100000|
+-------+-------+-----------------+------------------+

7. columns: It returns a list that contains the column names of the data.

print(df.columns)
['Name', 'Departments', 'Salary']

8. count(): It returns the count of the number of rows in the data.

print(df.count())  # 5

9. distinct(): It returns the number of distinct rows in the data

10. schema(): This method returns the schema of the data(dataframe).

print(df.schema)
StructType(List(StructField(Name,StringType,true),StructField(Departments,StringType,true),StructField(Salary,IntegerType,true)))

11. dtypes: It returns a list of tuples with column names and it’s data types.

print(df.dtypes)
[('Name', 'string'), ('Departments', 'string'), ('Salary', 'int')]
"""
