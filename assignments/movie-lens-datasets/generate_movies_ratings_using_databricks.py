"""
This file is used for to generate movies ratings.
Author: 'Rohit Pandey' <rohitpandey5491@gmail.com>
Date created: 27/09/2022
PySpark version: 3.2.1
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import *

spark = SparkSession.builder.appName('Movie Ratings').getOrCreate()

FILE_FORMAT = "csv"
SEPARATOR = "::"
MOVIES_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/movies.dat"
RATINGS_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/ratings.dat"
USERS_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/users.dat"

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


def join_dataframes(dataframe1, dataframe2, key):
    """This method is used for to join two dataframes based on common key"""
    return dataframe1.join(dataframe2, dataframe1[key] == dataframe2[key]).drop(dataframe2[key])


def get_popular_movies(dataframe):
    """This method is used for to get popular movies based on highest number of ratings"""
    return dataframe.groupBy('MovieID').agg(func.count(dataframe.UserID).alias("num_of_ratings")).orderBy(func.col("num_of_ratings").desc())


def get_top_rated_movies(dataframe):
    """This method is used to get top rated movies based on highest average rating"""
    return dataframe.groupBy('MovieID').agg(func.count(dataframe.Rating).alias("num_of_ratings"), func.avg(dataframe.Rating).alias("avg_ratings"))


def get_user_based_top_rated_movies(dataframe):
    """This method is used to get user based highest average top rated movies"""
    return dataframe.groupBy('UserID').agg(func.count(dataframe.Rating).alias("num_of_ratings"), func.avg(dataframe.Rating).alias("avg_ratings"))


# Create PySpark dataframes
movies_df = spark.read.format(FILE_FORMAT).schema(MOVIES_SCHEMA).option("header", "false").option("sep", SEPARATOR).load(MOVIES_DAT_FILE)
ratings_df = spark.read.format(FILE_FORMAT).schema(RATINGS_SCHEMA).option("header", "false").option("sep", SEPARATOR).load(RATINGS_DAT_FILE)
users_df = spark.read.format(FILE_FORMAT).schema(USERS_SCHEMA).option("header", "false").option("sep", SEPARATOR).load(USERS_DAT_FILE)

# Get most popular movies
most_popular_movies = get_popular_movies(ratings_df)
most_popular_movies_df = join_dataframes(most_popular_movies, movies_df, "MovieID")

# Get top rated movies
top_rated_movies = get_top_rated_movies(ratings_df)
top_rated_movies_df = join_dataframes(top_rated_movies, movies_df, "MovieID")

# Get user based highest average top rated movies
user_based_top_rated_movies = get_user_based_top_rated_movies(ratings_df)
user_based_top_rated_movies_df = join_dataframes(user_based_top_rated_movies, users_df, "UserID")

# Print desired result
top_10_rated_movies = top_rated_movies_df.where("num_of_ratings >= 10").orderBy("avg_ratings", ascending=False)
display(top_10_rated_movies)
max_age_group_ratings = user_based_top_rated_movies_df.groupBy('Age').agg(func.max('num_of_ratings')).orderBy("max(num_of_ratings)", ascending=False)
display(max_age_group_ratings)
