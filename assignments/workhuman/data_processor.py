import io
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import requests
import time
import yaml


def load_config():
    """
    Load configuration from config.yml.

    Returns:
    dict: The configuration dictionary.
    """
    with open("config.yml", 'r') as stream:
        config = yaml.safe_load(stream)
    return config


def timer(func):
    """
    Decorator to measure the execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timer
def retrieve_csv_data(url):
    """
    Retrieve CSV data from a given URL.

    Parameters:
    url (str): The URL of the CSV file.

    Returns:
    pd.DataFrame: The retrieved data as a DataFrame.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensure we got a valid response
    data = pd.read_csv(io.StringIO(response.text))
    return data


@timer
def process_data(df):
    """
    Process the data by filtering and aggregating values.

    Parameters:
    df (pd.DataFrame): The input data as a DataFrame.

    Returns:
    pd.DataFrame: The processed data.
    """
    # Lowercase all column names
    df.columns = map(str.lower, df.columns)

    # Filter out rows where 'value' is NaN
    df = df[df['value'].notna()]

    # Filter for 'First Year'
    df = df[df['statistic label'].str.contains("First Year", case=False)]

    # Convert 'year' to int for grouping
    df['year'] = df['year'].astype(int)

    # Group by 5-year periods and calculate sums
    df['year_group'] = (df['year'] // 5) * 5
    summary = df.groupby(['year_group', 'sex'])['value'].sum().reset_index()
    return summary


@timer
def write_data(df, csv_path, parquet_path):
    """
    Write data to CSV and Parquet formats.

    Parameters:
    df (pd.DataFrame): The data to write.
    csv_path (str): The path to save the CSV file.
    parquet_path (str): The path to save the Parquet file.
    """
    df.to_csv(csv_path, index=False)

    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_path)


@timer
def read_parquet_data(parquet_path):
    """
    Read data from a Parquet file.

    Parameters:
    parquet_path (str): The path to the Parquet file.

    Returns:
    pd.DataFrame: The data as a DataFrame.
    """
    df = pd.read_parquet(parquet_path)
    return df


# Main execution
if __name__ == "__main__":
    config = load_config()
    data = retrieve_csv_data(config['csv_url'])
    processed_data = process_data(data)
    write_data(processed_data, config['csv_output_path'], config['parquet_output_path'])

    # # Read the data from the Parquet file and print it
    # read_data = read_parquet_data(config['parquet_output_path'])
    # print(read_data.head())
