from pyspark.sql import functions as F
from pyspark.sql.types import *

FILE_FORMAT = "csv"
SEPARATOR = "::"
MOVIES_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/movies.dat"
RATINGS_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/ratings.dat"
USERS_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/users.dat"

# Create Our Own Schema
movies_schema = StructType([
    StructField('MovieID', IntegerType(), True),
    StructField('Title', StringType(), True),
    StructField('Genres', StringType(), True)
])
ratings_schema = StructType([
    StructField('UserID', IntegerType(), True),
    StructField('MovieID', IntegerType(), True),
    StructField('Rating', IntegerType(), True),
    StructField('Timestamp', IntegerType(), True)
])
users_schema = StructType([
    StructField('UserID', IntegerType(), True),
    StructField('Gender', StringType(), True),
    StructField('Age', IntegerType(), True),
    StructField('Occupation', IntegerType(), True),
    StructField('Zip-code', IntegerType(), True)
])


def join_dataframes(dataframe1, dataframe2, key):
    return dataframe1.join(dataframe2, dataframe1[key] == dataframe2[key]).drop(dataframe2[key])


def get_popular_movies(dataframe):
    return dataframe.groupBy('MovieID').agg(F.count(dataframe.UserID).alias("NoOfRatings")).orderBy(
        F.col("NoOfRatings").desc())


def get_top_rated_movies(dataframe):
    return dataframe.groupBy('MovieID').agg(F.count(dataframe.Rating).alias("NoOfRatings"),
                                            F.avg(dataframe.Rating).alias("avg_rating"))


def get_top_rated_movies_based_on_user_ratings(dataframe):
    return dataframe.groupBy('UserID').agg(F.count(dataframe.Rating).alias("NoOfRatings"),
                                           F.avg(dataframe.Rating).alias("avg_rating"))


def get_age_wise_top_ratings(dataframe):
    return dataframe.groupBy('UserID').agg(F.count(dataframe.Age).alias("NoOfRatings"),
                                           F.avg(dataframe.Age).alias("avg_rating"))


# Create PySpark dataframes
movies_df = spark.read.format(FILE_FORMAT).schema(movies_schema).option("header", "false").option("sep",
                                                                                                  SEPARATOR).load(
    MOVIES_DAT_FILE)
ratings_df = spark.read.format(FILE_FORMAT).schema(ratings_schema).option("header", "false").option("sep",
                                                                                                    SEPARATOR).load(
    RATINGS_DAT_FILE)
users_df = spark.read.format(FILE_FORMAT).schema(users_schema).option("header", "false").option("sep", SEPARATOR).load(
    USERS_DAT_FILE)

most_popular_movies = get_popular_movies(ratings_df)
# print(most_popular_movies.show(1))
most_popular_movies_df = join_dataframes(most_popular_movies, movies_df, "MovieID")
# print(movies_with_ratings_df.show(2))

top_rated_movies = get_top_rated_movies(ratings_df)
print(top_rated_movies.show(4))
top_rated_movies_df = join_dataframes(top_rated_movies, movies_df, "MovieID")
print(top_rated_movies_df.show(4))

top_rated_movies_with_atleast_10_ratings = top_rated_movies_df.where("NoOfRatings >= 10").orderBy("avg_rating",
                                                                                                  ascending=False)
# print(top_rated_movies_with_atleast_10_ratings.show(20))


temp1 = get_top_rated_movies_based_on_user_ratings(ratings_df)
print(temp1.show(2))
temp2 = join_dataframes(temp1, users_df, "UserID")
print(temp2.show(4))
# final_result = temp2.select([F.max(temp2.NoOfRatings)])
final_result = temp2.groupBy('Age').agg(F.max('NoOfRatings')).orderBy("max(NoOfRatings)", ascending=False)
print(final_result.show())

# age_wise_ratings_df = join_dataframes(users_df)
# print(age_wise_top_ratings.show(5))











