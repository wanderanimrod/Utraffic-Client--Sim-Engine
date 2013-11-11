from flask.ext import restful
from web_api.data import Data
from web_api.series import Series, OneSeries


def setup_api_routes(flask_app):
    api = restful.Api(flask_app)
    api.add_resource(Series, '/series/')
    api.add_resource(OneSeries, '/series/<int:series_id>/')
    api.add_resource(Data, '/series/<int:series_id>/data/')
