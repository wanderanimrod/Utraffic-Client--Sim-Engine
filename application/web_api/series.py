from flask import request
from flask.ext import restful
from application.models.series import Series as SeriesModel
from application.tests.test_utils.setup_some_static_data import fill_series_with_static_data
from application.web_api.persistent_data_server import get_data_server


class Series(restful.Resource):

    def post(self):
        data_server = get_data_server()
        series = SeriesModel()
        data_server.add_series(series)
        if request.args.get('debug') == 'true':
            fill_series_with_static_data(data_server, series.series_id)
        return series.json(), 201


class OneSeries(restful.Resource):

    def get(self, series_id):
        data_server = get_data_server()
        if data_server.get_series(series_id) is None:
            return {"error": "Series '%d' does not exist" % series_id}, 404
        series = data_server.get_series(series_id)
        return series.json(), 200