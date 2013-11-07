from flask import Flask
import flask

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

if __name__ == '__main__':
    app.run()