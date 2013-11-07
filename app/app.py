from flask import Flask
import flask
from web_api.routes import setup_api_routes as activate_web_api_routes

app = Flask(__name__)
app.debug = True

app.db = None
app.data_server = None


@app.route('/')
def get_data(visualisation=0):
    return flask.jsonify(
        {
            "data": [],
            "visualisation": visualisation
        }
    )

activate_web_api_routes(app)

if __name__ == '__main__':
    app.run()