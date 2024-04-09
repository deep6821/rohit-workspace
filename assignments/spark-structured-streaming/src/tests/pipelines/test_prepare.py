import unittest
from unittest.mock import MagicMock, patch
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pipelines.prepare import preprocess_data
from utility.utils import get_config_path


class TestPreprocessData(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.master("local[2]").appName("test").getOrCreate()
        self.spark.sparkContext.setLogLevel("ERROR")

    def tearDown(self):
        self.spark.stop()

    @patch('pipelines.prepare.get_spark_session')
    @patch('pipelines.prepare.load_config')
    @patch('pipelines.prepare.load_schema')
    @patch('pipelines.prepare.validate_schema')
    @patch('pipelines.prepare.write_to_csv')
    def test_preprocess_data(self, mock_write_to_csv, mock_validate_schema, mock_load_schema, mock_load_config,
                             mock_get_spark_session):
        # Mocking return value of get_spark_session
        mock_spark = MagicMock()
        mock_get_spark_session.return_value = mock_spark

        mock_load_config.return_value = {
            "output_path": "s3://bucket/output.csv",
            "processed_data_path": "s3://bucket/data.parquet"
        }
        mock_load_schema.return_value = StructType([
            StructField("difficulty", StringType(), True),
            StructField("avg_total_cooking_time", StringType(), True)
        ])
        mock_write_to_csv.return_value = MagicMock()

        # Mocking the Spark DataFrame
        data = [("recipe1", "PT1H", "PT30M"), ("recipe2", "PT2H", "PT20M")]
        schema = StructType([
            StructField("recipe", StringType(), True),
            StructField("cookTime", StringType(), True),
            StructField("prepTime", StringType(), True)
        ])
        df = self.spark.createDataFrame(data, schema)

        # Mocking the read.parquet method
        self.spark.read.parquet = MagicMock(return_value=df)

        # Mocking the validate_schema function to return the input DataFrame itself
        mock_validate_schema.return_value = df

        preprocess_data()

        mock_load_config.assert_called_once_with(get_config_path("configs/dev/aws_config.yml"))
        mock_load_schema.assert_called_once_with(get_config_path('schema/schemas.yml'), 'output_schema')
        mock_write_to_csv.assert_called_once()
        mock_get_spark_session.assert_called_once()  # Ensure get_spark_session is called


if __name__ == "__main__":
    unittest.main()
