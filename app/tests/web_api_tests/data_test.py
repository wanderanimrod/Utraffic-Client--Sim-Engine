from unittest import TestCase
from app import app
from tests.test_utils.json_parsers import extract_value_from_json, json_response_to_dict
from tests.test_utils.setup_some_static_data import make_static_data_points
from tests.web_api_tests.api_test_helpers import create_new_series


class SeriesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.app = app.test_client()

    def test_should_return_all_series_data_upon_get(self):
        expected_data = fetch_expected_data()
        series_id, _ = create_new_series(self.app, with_dummy_data=True)
        get = self.app.get('/series/%d/data/' % series_id)
        returned_data = extract_value_from_json(get.data, 'dataPoints')
        self.assertEquals(expected_data, returned_data)
        self.assertEquals(get.status_code, 200)


def fetch_expected_data():
    object_data_points = make_static_data_points()
    return object_data_points_list_to_json_data_points_list(object_data_points)


def object_data_points_list_to_json_data_points_list(data_points):
    json_data_points = []
    for data_point in data_points:
        json_data_points.append(data_point.json())
    return json_data_points