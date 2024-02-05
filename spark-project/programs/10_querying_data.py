from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('practise').getOrCreate()
file_location = r"C:\office\rohit-workspace\spark-project\inputs\querying-data.csv"
df = spark.read.csv(file_location, header=True, inferSchema=True)

"""
1. select: It is used to select single or multiple columns using the names of the columns.

df = df.select('Name').show()
df = df.select(['Name', 'EXPERIENCE']).show()

2. filter: Filter the data based on the given condition, you can also give multiple conditions
  using AND(&), OR(|), and NOT(~) operators.

df = df.filter("Salary<=50000")
print(df.show())

df = df.filter("SALARY<=50000").select(['NAME'])
                OR
df = df.filter(df["SALARY"]<=50000).select(['NAME'])
print(df.show())

3. between: This method returns either True or False if the passed values in the between method.

df = df.filter(df['Salary'].between(80000, 90000))
print(df.show())

4. when: It returns 0 or 1 depending on the given condition.

df = df.select('Name', 'Departments', df.when(df["Salary"]<=50000).otherwise(0))
print(df.show())

5. like: It is similar to the like operator in SQL

6. groupBy: The name itself explains that it groups the data by the given column name and it can
   perform different operations such as sum, mean, min, max, e.t.c.
   
df = df.groupBy('Name').sum()
print(df.show())
+-------+-----------+
|   Name|sum(Salary)|
+-------+-----------+
|Adhyeta|     150000|
|  Rohit|     260000|
+-------+-----------+

7. agg: PySpark provides built-in standard Aggregate functions defines in DataFrame API, these 
   come in handy when we need to make aggregate operations on columns of the data. Aggregate 
   functions operate on a group of rows and calculate a single return value for every group.
   
df = df.agg({'Salary': 'sum'})
print(df.show())
+-----------+
|sum(Salary)|
+-----------+
|     410000|
+-----------+
"""

