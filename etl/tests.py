import unittest

from utils import soda_montgomery_request


class TestUtils(unittest.TestCase):

    def test_soda_request(self):
        start_date = "2023-12-01"
        end_date = "2023-12-31"
        df = soda_montgomery_request('incidents', start_date, end_date)
        self.assertGreater(len(df), 900)