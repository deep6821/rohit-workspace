import os
import pandas as pd
import unittest
from data_processor import retrieve_csv_data, process_data, write_data, load_config


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.config = load_config()

        # Sample data for testing
        self.sample_data = pd.DataFrame({
            'statistic label': [
                                   'Entrants to First Year of Junior Cycle',
                                   'First Year Entrants who entered First Year of Senior Cycle',
                                   'First Year Entrants who entered Second Year of Junior Cycle',
                                   'First Year Entrants who entered Second Year of Senior Cycle',
                                   'First Year Entrants who entered Third Year of Junior Cycle',
                                   'First Year Entrants who sat the Junior Certificate',
                                   'First Year Entrants who sat the Junior Certificate'
                               ] * 2,
            'year': [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004],
            'sex': ['Male', 'Female'] * 7,
            'value': [10, 20, 30, 40, 50, 60, 70, 15, 25, 35, 45, 55, 65, 75]
        })

    def test_retrieve_csv_data(self):
        data = retrieve_csv_data(self.config['csv_url'])
        self.assertIsInstance(data, pd.DataFrame)

    def test_process_data(self):
        processed_data = process_data(self.sample_data)

        expected_data = pd.DataFrame({
            'year_group': [1990, 1990, 1995, 1995, 2000, 2000],
            'sex': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
            'value': [60, 40, 75, 145, 165, 110]
        })

        # Sort both DataFrames by 'year_group' and 'sex'
        processed_data = processed_data.sort_values(by=['year_group', 'sex']).reset_index(drop=True)
        expected_data = expected_data.sort_values(by=['year_group', 'sex']).reset_index(drop=True)

        pd.testing.assert_frame_equal(processed_data, expected_data)

    def test_write_data(self):
        write_data(self.sample_data, self.config['csv_output_path'], self.config['parquet_output_path'])
        self.assertTrue(os.path.exists(self.config['csv_output_path']))
        self.assertTrue(os.path.exists(self.config['parquet_output_path']))


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
