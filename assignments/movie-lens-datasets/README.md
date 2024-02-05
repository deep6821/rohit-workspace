# Coding Challenge: Movie Ratings

## Setup

* Use the dataset provided at the `data` folder. You can find a documentation here: https://files.grouplens.org/datasets/movielens/ml-1m-README.txt.
* Educate yourself about the format of the provided data set.
* Create a project in the language of your choice, load the data and answer the questions below (results should be written to STDOUT).

## Tasks

1. Which are the Top 10 best rated movies (consider only movies which have at least 10 ratings)?
2. Which age group give the most ratings overall?


## Additional information
* You are free to choose language, frameworks and toolings.
* Please document what you are doing. If you manipulate the data before reading/importing please explain what you did (and why).
* Please document how to run the code.


## Steps required to run Spark based applications using Python locally
1. Install and setup Python --> https://www.python.org/downloads/
2. Install and setup any IDE(Example: PyCharm) --> https://www.jetbrains.com/help/pycharm/installation-guide.html
3. Install and setup PySpark  --> pip install pyspark==3.2.1
4. Add environment variables
a) SPARK_HOME=/ <PyCharm Installation Path>/Spark/venv/lib/python3.6/site-packages/pyspark
b) PYTHONPATH=$SPARK_HOME/python
5. Run PySpark applications: python <file_name>
   Example: python generate_movies_ratings.py
   
## Steps required to run PySpark using DataBricks platform
Community version sign-up URL:  https://community.cloud.databricks.com/login.html   
   
1. Download input zip file: https://github.com/xing/test_movielens-deep6821/blob/master/data/ml-1m.zip
2. Extract zip file and upload required files to DataBricks File System
   <img width="663" alt="image" src="https://user-images.githubusercontent.com/13431228/192574190-263e4619-2c2c-43ce-8837-dd462cb8b014.png">

   Example: I have created a input directory in DBFS and uploaded all the required files i.e. movies.dat, ratings.dat, users.dat
3. Create cluster
   
   <img width="568" alt="image" src="https://user-images.githubusercontent.com/13431228/192577882-d10e196b-e923-400e-a5a7-8fcdbf98fedb.png">

4. Create a Notebook. Example: Movie Lens Data
5. Write all the code inside a Notebook and run the code over there
   ![image](https://user-images.githubusercontent.com/13431228/192579093-b4664349-2fa8-4622-9810-2c007fff83be.png)

```ruby
from pyspark.sql import functions as func
from pyspark.sql.types import *

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

```


