from flask.ext import restful
from models.series import Series as SeriesModel
from tests.test_utils.setup_some_static_data import fill_series_with_static_data
from web_api.persistent_data_server import get_data_server


class OneSeries(restful.Resource):

    def get(self, series_id):
        data_server = get_data_server()
        try:
            data_points = data_server.get_data_for_series(series_id)
            #Restore the data so we can read it multiple times (overriding designed behaviour)
            fill_series_with_static_data(data_server, series_id)
            json_data_points = []
            for data_point in data_points:
                json_data_points.append(data_point.json())
            return {'dataPoints': json_data_points, "series": series_id}, 200
        except Exception, ex:
            return {"error": ex.message}, 404


class Series(restful.Resource):

    def post(self):
        data_server = get_data_server()
        series = SeriesModel()
        series_id = data_server.add_series(series)
        #Take the next line out in prod
        fill_series_with_static_data(data_server, series.series_id)
        return {'seriesId': series_id}, 201