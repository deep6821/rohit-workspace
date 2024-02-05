from pyspark import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('practise').getOrCreate()
employee_data = [
    {"emp_id": 1, "name": "Smith", "superior_emp_id": -1, "year_joined": "2018", "emp_dept_id": "10", "gender": "M", "salary": 3000},
    {"emp_id": 2, "name": "Rose", "superior_emp_id": 1, "year_joined": "2010", "emp_dept_id": "20", "gender": "M", "salary": 4000}
]

rdd = spark.sparkContext.parallelize(employee_data)
print(type(rdd))  # <class 'pyspark.rdd.RDD'>
df = rdd.toDF() # DataFrame[emp_dept_id: string, emp_id: bigint, gender: string, name: string, salary: bigint, superior_emp_id: bigint, year_joined: string]
print(df)  #
print(type(df))  # <class 'pyspark.sql.dataframe.DataFrame'>

# ----------------------------------------------------------------------------

df1 = spark.createDataFrame(rdd).toDF("emp_id", "name", "superior_emp_id", "year_joined", "emp_dept_id", "gender", "salary")


