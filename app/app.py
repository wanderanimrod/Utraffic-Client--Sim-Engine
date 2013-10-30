from flask import Flask, render_template
import flask
import redis
from tests.test_utils.setup_some_static_data import get_data_server

app = Flask(__name__)
app.debug = True

app.db = None
app.data_server = None


@app.route('/')
def index():
    app.data_server = get_data_server()
    return render_template('index.html')


@app.route('/get_data/<visualisation>/')
def get_data(visualisation=0):
    return flask.jsonify(
        {
            "data": [],
            "visualisation": visualisation
        }
    )

if __name__ == '__main__':
    app.run()


def get_db():
    if app.db is None:
        app.db = redis.StrictRedis(host='localhost', port=6379, db=0)
    return app.db