"""
This file is used for to write all custom schema.
Author: 'Rohit Pandey' <rohitpandey5491@gmail.com>
Date created: 27/09/2022
Python version: 3.6
PySpark version: 3.2.1
"""

from pyspark.sql.types import *

# Create custom schema
MOVIES_SCHEMA = StructType([
    StructField('MovieID', IntegerType(), True),
    StructField('Title', StringType(), True),
    StructField('Genres', StringType(), True)
])
RATINGS_SCHEMA = StructType([
    StructField('UserID', IntegerType(), True),
    StructField('MovieID', IntegerType(), True),
    StructField('Rating', IntegerType(), True),
    StructField('Timestamp', IntegerType(), True)
])
USERS_SCHEMA = StructType([
    StructField('UserID', IntegerType(), True),
    StructField('Gender', StringType(), True),
    StructField('Age', IntegerType(), True),
    StructField('Occupation', IntegerType(), True),
    StructField('ZipCode', IntegerType(), True)
])
