from unittest import TestCase
from app import app
from tests.test_utils.json_parsers import extract_value_from_json


class SeriesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        cls.app = app.test_client()

    def test_should_create_series_upon_post(self):
        post = self.app.post('/series/')
        series_id = extract_value_from_json(post.data, 'seriesId')
        get = self.app.get('/series/%d/data' % series_id)
        returned_series_id = extract_value_from_json(get.data, 'seriesId')
        self.assertEquals(series_id, returned_series_id)

    def create_new_series(self):
        post = self.app.post('/series/')
        return extract_value_from_json(post.data, 'seriesId')

