from flask.ext import restful
from application.web_api.series import Series
from application.web_api.data import Data
from application.web_api.series import OneSeries


def setup_api_routes(flask_app):
    api = restful.Api(flask_app)
    api.add_resource(Series, '/series/')
    api.add_resource(OneSeries, '/series/<int:series_id>/')
    api.add_resource(Data, '/series/<int:series_id>/data/')
