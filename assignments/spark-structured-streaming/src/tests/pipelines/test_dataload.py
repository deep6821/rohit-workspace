import unittest
from unittest.mock import patch, call
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pipelines.dataload import process_data
from utility.utils import get_config_path


class TestDataload(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.getOrCreate()

    @patch('pipelines.dataload.setup_logging')
    @patch('pipelines.dataload.get_spark_session')
    @patch('pipelines.dataload.load_config')
    @patch('pipelines.dataload.load_schema')
    @patch('pipelines.dataload.get_kafka_stream')
    @patch('pipelines.dataload.validate_schema')
    @patch('pipelines.dataload.write_to_s3_stream')
    @patch('pipelines.dataload.get_latest_processed_date')
    def test_process_data_success(
            self,
            mock_get_latest_processed_date,
            mock_write_to_s3_stream,
            mock_validate_schema,
            mock_get_kafka_stream,
            mock_load_schema,
            mock_load_config,
            mock_get_spark_session,
            mock_setup_logging
    ):
        # Mock the external dependencies
        mock_setup_logging.return_value = None
        mock_get_spark_session.return_value = self.spark
        mock_load_config.return_value = {
            'aws_access_key': 'test_key',
            'aws_secret_key': 'test_secret',
            'region': 'us-east-1'
        }
        mock_load_schema.return_value = StructType([StructField("name", StringType(), nullable=False)])
        mock_get_kafka_stream.return_value = self.spark.createDataFrame([{'name': 'Baked Ziti'}])
        mock_validate_schema.return_value = self.spark.createDataFrame([{'name': 'Baked Ziti'}])
        mock_get_latest_processed_date.return_value = '2023-04-01'
        mock_write_to_s3_stream.return_value = None

        # Call the function under test
        process_data()

        # Assert that the external dependencies were called as expected
        mock_setup_logging.assert_called_once()
        mock_get_spark_session.assert_called_once()
        mock_load_config.assert_has_calls([
            call(get_config_path('configs/dev/aws_config.yml')),
            call(get_config_path('configs/dev/kafka_config.yml'))
        ])
        mock_load_schema.assert_called_once_with(get_config_path('schema/schemas.yml'), 'input_schema')
        mock_get_kafka_stream.assert_called_once()
        mock_validate_schema.assert_called_once()
        mock_get_latest_processed_date.assert_called_once()
        mock_write_to_s3_stream.assert_called_once()

    def test_process_data_error(self):
        # Mock the external dependencies to raise an exception
        with patch('pipelines.dataload.setup_logging'), \
                patch('pipelines.dataload.get_spark_session'), \
                patch('pipelines.dataload.load_config',
                      return_value={
                          'aws_access_key': 'test_key',
                          'aws_secret_key': 'test_secret',
                          'region': 'us-east-1'
                      }), \
                patch('pipelines.dataload.load_schema',
                      return_value=StructType([StructField("name", StringType(), nullable=False)])), \
                patch('pipelines.dataload.get_kafka_stream', side_effect=Exception('Kafka connection error')), \
                patch('pipelines.dataload.validate_schema'), \
                patch('pipelines.dataload.write_to_s3_stream'):
            with self.assertRaises(Exception) as context:
                process_data()

            self.assertEqual(str(context.exception), 'Kafka connection error')

    def tearDown(self):
        self.spark.stop()


if __name__ == '__main__':
    unittest.main()
