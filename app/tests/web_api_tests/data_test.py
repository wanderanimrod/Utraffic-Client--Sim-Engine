from unittest import TestCase
from app import app


class SeriesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.app = app.test_client()

    def test_should_return_all_series_data_upon_creation_of_series(self):
        pass