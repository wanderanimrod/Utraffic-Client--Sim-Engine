from flask.ext import restful
from models.series import Series as SeriesModel
from web_api.persistent_data_server import get_data_server


class OneSeries(restful.Resource):

    def get(self, series_id):
        return {'series': series_id}


class Series(restful.Resource):

    def post(self):
        data_server = get_data_server()
        series_id = data_server.add_series(SeriesModel())
        return {'seriesId': series_id}, 201