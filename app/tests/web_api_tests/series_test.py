from unittest import TestCase
from app import app
from tests.test_utils.json_parsers import extract_value_from_json, json_string_has_expected_keys, json_response_to_dict
from tests.web_api_tests.api_test_helpers import create_new_series


class SeriesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.app = app.test_client()

    def test_should_create_series_upon_post(self):
        series_id, post = create_new_series(self.app)
        get = self.app.get('/series/%d/' % series_id)
        returned_series_id = extract_value_from_json(get.data, 'id')
        self.assertEquals(series_id, returned_series_id)
        self.assertEquals(post.status_code, 201)

    def test_should_return_all_details_on_series_upon_request_on_the_series_resource(self):
        series_id, _ = create_new_series(self.app)
        get = self.app.get('/series/%d/' % series_id)
        expected_keys = ['id', 'status']
        self.assertTrue(json_string_has_expected_keys(get.data, expected_keys))
        self.assertEquals(get.status_code, 200)

    def test_should_throw_404_when_get_request_for_series_with_inexistent_id_is_made(self):
        inexistent_series_id = 1503
        get = self.app.get('/series/%d/' % inexistent_series_id)
        expected_get_result = {"error": "Series '%d' does not exist" % inexistent_series_id}
        self.assertEquals(expected_get_result, json_response_to_dict(get.data))
        self.assertEquals(get.status_code, 404)