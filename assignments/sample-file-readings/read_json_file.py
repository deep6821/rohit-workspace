import json
import pandas as pd
# from pyspark.sql import SparkSession
from tqdm import tqdm


def read_json(file_path, data_library='pandas'):
    """
    Read JSON file using Pandas or PySpark based on the specified data library.
    
    Parameters:
        file_path (str): Path to the JSON file.
        data_library (str): Data library to use for reading the JSON file ('pandas' or 'pyspark').
    
    Returns:
        DataFrame: DataFrame containing the data loaded from the JSON file.
    """
    if data_library == 'pandas':
        try:
            # data = []
            # with open(file_path, "r") as f:
            #     for line in tqdm(f):
            #         data.append(json.loads(line))
            # df = pd.DataFrame(data)
            
            df = pd.read_json(file_path, orient='records',lines=True)
        except Exception as e:
            print("Error:", e)
            df = None
    elif data_library == 'pyspark':
        pass
        # try:
        #     spark = SparkSession.builder.appName("ReadJSON").getOrCreate()
        #     df = spark.read.json(file_path)
        # except Exception as e:
        #     print("Error:", e)
        #     df = None
    else:
        print("Error: Invalid data library specified. Supported libraries are 'pandas' and 'pyspark'.")
        df = None
    
    return df
