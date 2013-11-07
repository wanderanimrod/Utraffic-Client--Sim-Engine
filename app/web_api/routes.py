from flask.ext import restful
from web_api.series import Series


def setup_api_routes(flask_app):
    api = restful.Api(flask_app)
    api.add_resource(Series, '/series/')