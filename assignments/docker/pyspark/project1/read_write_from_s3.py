import boto3
import os
from datetime import datetime
from dotenv import load_dotenv


# Load environment variables from .env file (optional)
load_dotenv()


def read_csv_files_from_directory():
    local_directory = os.getenv("LOCAL_DIRECTORY")
    # Create the path to the data folder
    input_data_dir = os.path.join(os.getcwd(), local_directory)
    # Check if the directory exists
    if not os.path.exists(input_data_dir):
        raise FileNotFoundError(f"Directory '{input_data_dir}' does not exist.")
    else:
        # Iterate through all files in the directory
        for file_name in os.listdir(input_data_dir):
            if file_name.endswith(".csv"):
                file_path = os.path.join(input_data_dir, file_name)
                print(file_path)

def download_s3_object_as_csv(object_key=None):
    """
    Downloads an object from the specified S3 bucket and saves it as a CSV file with a timestamp.

    Args:
        object_key (str, optional): Key (filename) of the object to download (can be None for all objects).
    """
    # Access AWS credentials
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    region_name = os.getenv("AWS_REGION_NAME")
    bucket_name = os.getenv("AWS_S3_BUCKET_NAME")
    local_directory = os.getenv("LOCAL_DIRECTORY")

    s3_resource = boto3.resource(
        service_name="s3",
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        bucket = s3_resource.Bucket(bucket_name)

        # Create the path to the data folder
        input_data_dir = os.path.join(os.getcwd(), local_directory)

        # Check if the data folder exists, if not, create it
        if not os.path.exists(input_data_dir):
            os.makedirs(input_data_dir)

        # Iterate through all objects in the bucket
        for obj in bucket.objects.all():
            key = obj.key

            # Download only files with .csv extension (modify if needed)
            if key.endswith(".csv") and (object_key is None or key == object_key):
                # Generate a timestamp string
                timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

                # Construct local filename with timestamp and key
                filename = os.path.join(input_data_dir, f"{os.path.splitext(os.path.basename(key))[0]}_{timestamp}.csv")

                try:
                    body = obj.get()['Body'].read()
                    # print("Key: ", key)
                    # print("Body: ", body)
                    with open(filename, "wb") as f:
                        f.write(body)
                        print(f"Downloaded file: {filename}")
                except Exception as e:
                    print(f"Error downloading {key}: {e}")

    except Exception as e:
        print(f"Error accessing bucket: {e}")


# Download all CSV files with timestamps in a specific directory
download_s3_object_as_csv()
