from flask.ext import restful
from models.series import Series as SeriesModel
from web_api.persistent_data_server import get_data_server


class OneSeries(restful.Resource):

    def get(self, series_id):
        data_server = get_data_server()
        try:
            data_points = data_server.get_data_for_series(series_id)
            return {'dataPoints': data_points, "series": series_id}, 200
        except Exception, ex:
            return {"error": ex.message}, 404


class Series(restful.Resource):

    def post(self):
        data_server = get_data_server()
        series_id = data_server.add_series(SeriesModel())
        return {'seriesId': series_id}, 201