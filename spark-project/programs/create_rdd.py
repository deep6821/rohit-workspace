from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

employee_data = [
    {"emp_id": 1, "name": "Smith", "superior_emp_id": -1, "year_joined": "2018", "emp_dept_id": "10", "gender": "M", "salary": 3000},
    {"emp_id": 2, "name": "Rose", "superior_emp_id": 1, "year_joined": "2010", "emp_dept_id": "20", "gender": "M", "salary": 4000}
]
file_path = "dbfs:/FileStore/shared_uploads/input/sample.csv"
file_format = "csv"

# 1. Create RDD from parallelize
spark = SparkSession.builder.appName('practise').getOrCreate()
rdd = spark.sparkContext.parallelize(employee_data)

# 2. Create RDD from external Data source


