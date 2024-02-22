import pandas as pd
from pyspark.sql import SparkSession

def read_csv(file_path, data_library='pandas'):
    """
    Read CSV file using Pandas or PySpark based on the specified data library.
    
    Parameters:
        file_path (str): Path to the CSV file.
        data_library (str): Data library to use for reading the CSV file ('pandas' or 'pyspark').
    
    Returns:
        DataFrame: DataFrame containing the data loaded from the CSV file.
    """
    if data_library == 'pandas':
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print("Error:", e)
            df = None
    elif data_library == 'pyspark':
        try:
            spark = SparkSession.builder.appName("ReadCSV").getOrCreate()
            df = spark.read.csv(file_path, header=True, inferSchema=True)
            # df = spark.read.format("csv").options(header='true', inferSchema='true').load(file_path)
            # df = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)
            # df = spark.read.load(file_path, format="csv", header="true", inferSchema="true")

        except Exception as e:
            print("Error:", e)
            df = None
    else:
        print("Error: Invalid data library specified. Supported libraries are 'pandas' and 'pyspark'.")
        df = None
    
    return df


if __name__ == "__main__":
    file_path = "path/to/your/csv/file.csv"
    data_pandas = read_csv(file_path, data_library='pandas')
    data_pyspark = read_csv(file_path, data_library='pyspark')
