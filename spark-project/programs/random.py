data1 = [
    {"id": 1, "name": "India", "iso_code": "IND"},
    {"id": 2, "name": "United State of America", "iso_code": "USA"},
    {"id": 3, "name": "Australia", "iso_code": "AUS"}
]
data2 = [
    {"geographics": "India", "pos": "lat1-long1", "matrix": "temp",
     "value": 26},
    {"geographics": "United Kingdom", "pos": "lat2-long2",
     "matrix": "humidity", "value": 27},
]

# output = [
#     {"timestamp": "", "geographics": "India", "iso_code":"IND",
#     "pos":"lat1-long1", "matrx":"temp", "value": 26},
#     {"timestamp": "", "geographics": "", "iso_code":"IND",
#     "pos":"lat1-long1", "matrx":"temp", "value": 26},

# ]

df1 = spark.createDataFrame(data=data1)
df2 = spark.createDataFrame(data=data2)
df3 = df1.join(df2, df1["name"] == df2["geographics"], how="full")
print(df3.show())



from pyspark.sql.types import *

FILE_FORMAT = "csv"
SEPARATOR = "::"
MOVIES_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/movies.dat"
RATINGS_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/ratings.dat"
USERS_DAT_FILE = "dbfs:/FileStore/shared_uploads/input/users.dat"

# Create Our Own Schema
movies_schema =StructType([
    StructField('MovieID', IntegerType(), True),
    StructField('Title', StringType(), True),
    StructField('Genres', StringType(), True)
])
ratings_schema =StructType([
    StructField('UserID', IntegerType(), True),
    StructField('MovieID', IntegerType(), True),
    StructField('Rating', IntegerType(), True),
    StructField('Timestamp', IntegerType(), True)
])
users_schema =StructType([
    StructField('UserID', IntegerType(), True),
    StructField('Gender', StringType(), True),
    StructField('Age', IntegerType(), True),
    StructField('Occupation', IntegerType(), True),
    StructField('Zip-code', IntegerType(), True)
])
movies_df = spark.read.format(FILE_FORMAT).schema(movies_schema).option("header", "false").option("sep", SEPARATOR).load(MOVIES_DAT_FILE)
ratings_df = spark.read.format(FILE_FORMAT).schema(ratings_schema).option("header", "false").option("sep", SEPARATOR).load(RATINGS_DAT_FILE)
users_df = spark.read.format(FILE_FORMAT).schema(users_schema).option("header", "false").option("sep", SEPARATOR).load(USERS_DAT_FILE)

print(movies_df.show(2))
print(ratings_df.show(2))
print(users_df.show(2))

join_df = movies_df.join(ratings_df, movies_df.MovieID==ratings_df.MovieID).drop(ratings_df.MovieID)
print(join_df.show(5))


# struct_schema=StructType(fields=movies_schema)
# print(struct_schema)

# def parse_file(element):
#     return element.split('::', 3)

# movies_dataset = sc.textFile(MOVIES_DAT_FILE)
# print(movies_dataset.collect())


# movies_dataset = movies_dataset.map(parse_file)
# ratings_dataset = sc.textFile(RATINGS_DAT_FILE)
# ratings_dataset = ratings_dataset.map(parse_file)
# movies_df = movies_dataset.toDF()
# ratings_df = ratings_dataset.toDF()
# print(movies_df.show(3))
# print(ratings_df.show(3))

