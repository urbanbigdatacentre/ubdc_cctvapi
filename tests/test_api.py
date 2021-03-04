import unittest
import pytest


class TestCctvAPI(unittest.TestCase):

    def test_get_data(self):
        from ubdc_cctvapi.api import CctvApi
        api = CctvApi()

        data = api.get_data_for_location(location='Glasgow_Green_monument', from_date='2020-06-07',
                                         to_date='2020-06-07')

        self.assertIsInstance(data, dict)

    def test_get_data_error(self):
        from ubdc_cctvapi.api import CctvApi
        api = CctvApi()

        with pytest.raises(ValueError) as excinfo:
            data = api.get_data_for_location(location='Glasgow_green_monument', from_date='2020-06-07',
                                             to_date='2020-06-07')
