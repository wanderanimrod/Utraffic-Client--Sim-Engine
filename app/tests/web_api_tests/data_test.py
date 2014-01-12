from unittest import TestCase
from app import app
from tests.test_utils.json_parsers import extract_value_from_json, json_response_to_dict
from tests.test_utils.setup_some_static_data import make_static_data_points
from tests.web_api_tests.api_test_helpers import create_new_series


class DataTest(TestCase):

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

    def test_should_include_series_id_in_get_data(self):
        series_id, _ = create_new_series(self.app, with_dummy_data=True)
        get = self.app.get('/series/%d/data/' % series_id)
        series_id_in_returned_data = extract_value_from_json(get.data, 'seriesId')
        self.assertEquals(series_id_in_returned_data, series_id)

    def test_should_include_series_status_in_get_data(self):
        series_id, _ = create_new_series(self.app, with_dummy_data=True)
        get = self.app.get('/series/%d/data/' % series_id)
        series_status = extract_value_from_json(get.data, 'seriesStatus')
        self.assertEquals(series_status, "active")

    def test_should_return_series_with_status_complete_if_request_specifies_series_as_dummy(self):
        series_id, _ = create_new_series(self.app, with_dummy_data=True)
        get = self.app.get('/series/%d/data/' % series_id + '?dummy_series=true')
        series_status = extract_value_from_json(get.data, 'seriesStatus')
        self.assertEquals(series_status, "complete")

    def test_should_return_404_if_data_is_requested_for_inexistent_series(self):
        inexistent_series_id = 1503
        get = self.app.get('/series/%d/data/' % inexistent_series_id)
        expected_get_result = {"error": "Series '%d' does not exist" % inexistent_series_id}
        self.assertEquals(expected_get_result, json_response_to_dict(get.data))
        self.assertEquals(get.status_code, 404)


def fetch_expected_data():
    object_data_points = make_static_data_points()
    return object_data_points_list_to_json_data_points_list(object_data_points)


def object_data_points_list_to_json_data_points_list(data_points):
    json_data_points = []
    for data_point in data_points:
        json_data_points.append(data_point.json())
    return json_data_points