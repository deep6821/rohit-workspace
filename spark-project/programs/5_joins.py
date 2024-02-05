"""
Reference: https://sparkbyexamples.com/pyspark/pyspark-join-explained-with-examples/

PySpark Join Methods
1. INNER
2. LEFT OUTER JOIN
3. RIGHT OUTER JOIN
4. FULL OUTER
5. LEFT ANTI
6. LEFT SEMI

join Type Syntax:
df1.join(df2, df1.key=df2.key, join_type)


"""
spark = SparkSession.builder.appName('practise').getOrCreate()

employee_data = [
    (1, "Smith", -1, "2018", "10", "M", 3000),
    (2, "Rose", 1, "2010", "20", "M", 4000),
    (3, "Williams", 1, "2010", "10", "M", 1000),
    (4, "Jones", 2, "2005", "10", "F", 2000),
    (5, "Brown", 2, "2010", "40", "", -1),
    (6, "Brown", 2, "2010", "50", "", -1)
]
employee_columns = ["emp_id", "name", "superior_emp_id", "year_joined", "emp_dept_id", "gender", "salary"]

department_data = [
    ("Finance", 10),
    ("Marketing", 20),
    ("Sales", 30),
    ("IT", 40)
]
department_columns = ["dept_name", "dept_id"]

employee_df = spark.createDataFrame(data=employee_data, schema=employee_columns)
department_df = spark.createDataFrame(data=department_data, schema=department_columns)
print(employee_df.show())
print(department_df.show())

"""
+------+--------+---------------+-----------+-----------+------+------+
|emp_id|    name|superior_emp_id|year_joined|emp_dept_id|gender|salary|
+------+--------+---------------+-----------+-----------+------+------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|
|     2|    Rose|              1|       2010|         20|     M|  4000|
|     3|Williams|              1|       2010|         10|     M|  1000|
|     4|   Jones|              2|       2005|         10|     F|  2000|
|     5|   Brown|              2|       2010|         40|      |    -1|
|     6|   Brown|              2|       2010|         50|      |    -1|
+------+--------+---------------+-----------+-----------+------+------+


+---------------+-------------+
|department_name|department_id|
+---------------+-------------+
|        Finance|           10|
|      Marketing|           20|
|          Sales|           30|
|             IT|           40|
+---------------+-------------+
"""

# Inner Join --> Returns records that have matching values in both tables
inner_join_df = employee_df.join(department_df,employee_df.emp_dept_id == department_df.dept_id, "inner")
print(inner_join_df.show())
"""
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|    name|superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|  Finance|     10|
|     3|Williams|              1|       2010|         10|     M|  1000|  Finance|     10|
|     4|   Jones|              2|       2005|         10|     F|  2000|  Finance|     10|
|     2|    Rose|              1|       2010|         20|     M|  4000|Marketing|     20|
|     5|   Brown|              2|       2010|         40|      |    -1|       IT|     40|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
"""
# Left Join --> Returns all records from the left table (table1), and the matching records from the right table (table2)
left_join_df = employee_df.join(department_df,employee_df.emp_dept_id == department_df.dept_id, "left")
print(left_join_df.show())
"""
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|    name|superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|  Finance|     10|
|     3|Williams|              1|       2010|         10|     M|  1000|  Finance|     10|
|     4|   Jones|              2|       2005|         10|     F|  2000|  Finance|     10|
|     2|    Rose|              1|       2010|         20|     M|  4000|Marketing|     20|
|     5|   Brown|              2|       2010|         40|      |    -1|       IT|     40|
|     6|   Brown|              2|       2010|         50|      |    -1|     null|   null|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
"""

# Right Join --> Returns all records from the right table (table2), and the matching records from the left table (table1)
right_join_df = employee_df.join(department_df,employee_df.emp_dept_id == department_df.dept_id, "right")
print(right_join_df.show())
"""
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|    name|superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|  Finance|     10|
|     3|Williams|              1|       2010|         10|     M|  1000|  Finance|     10|
|     4|   Jones|              2|       2005|         10|     F|  2000|  Finance|     10|
|     2|    Rose|              1|       2010|         20|     M|  4000|Marketing|     20|
|  null|    null|           null|       null|       null|  null|  null|    Sales|     30|
|     5|   Brown|              2|       2010|         40|      |    -1|       IT|     40|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
"""

# Full Join --> Returns all records when there is a match in left (table1) or right (table2) table records.
full_outer_join_df = employee_df.join(department_df,employee_df.emp_dept_id == department_df.dept_id, "full")
print(full_outer_join_df.show())
"""
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|    name|superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|  Finance|     10|
|     3|Williams|              1|       2010|         10|     M|  1000|  Finance|     10|
|     4|   Jones|              2|       2005|         10|     F|  2000|  Finance|     10|
|     2|    Rose|              1|       2010|         20|     M|  4000|Marketing|     20|
|  null|    null|           null|       null|       null|  null|  null|    Sales|     30|
|     5|   Brown|              2|       2010|         40|      |    -1|       IT|     40|
|     6|   Brown|              2|       2010|         50|      |    -1|     null|   null|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
"""

# Left Outer Join --> Returns all records when there is a match in either left or right table
left_outer_join_df = employee_df.join(department_df,employee_df.emp_dept_id == department_df.dept_id, "leftouter")
print(left_outer_join_df.show())
"""
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|emp_id|    name|superior_emp_id|year_joined|emp_dept_id|gender|salary|dept_name|dept_id|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
|     1|   Smith|             -1|       2018|         10|     M|  3000|  Finance|     10|
|     3|Williams|              1|       2010|         10|     M|  1000|  Finance|     10|
|     4|   Jones|              2|       2005|         10|     F|  2000|  Finance|     10|
|     2|    Rose|              1|       2010|         20|     M|  4000|Marketing|     20|
|     5|   Brown|              2|       2010|         40|      |    -1|       IT|     40|
|     6|   Brown|              2|       2010|         50|      |    -1|     null|   null|
+------+--------+---------------+-----------+-----------+------+------+---------+-------+
"""

# Right Outer Join --> Returns all records when there is a match in either left or right table
right_outer_join_df = employee_df.join(department_df,employee_df.emp_dept_id == department_df.dept_id, "leftouter")
print(left_outer_join_df.show())
