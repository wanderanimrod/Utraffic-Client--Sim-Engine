from flask.ext import restful


class Series(restful.Resource):

    def get(self):
        return {'hello': 'world'}

