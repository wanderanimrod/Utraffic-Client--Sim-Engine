from flask import Flask
import flask
from web_api.routes import setup_api_routes as activate_web_api_routes

app = Flask(__name__)
app.debug = True
app.db = None


@app.route('/')
def get_data():
    return flask.jsonify({"Message": "The Utraffic API is now running!"})

activate_web_api_routes(app)

if __name__ == '__main__':
    app.run()