from unittest import TestCase
from application.models.data_point import DataPoint


class DataPointTest(TestCase):

    def test_should_make_json_of_itself(self):
        data_point = DataPoint(10, 0)
        json = data_point.json()
        self.assertEquals(json, {'value': 10, 'time': 0})