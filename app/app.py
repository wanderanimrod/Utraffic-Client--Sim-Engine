from flask import Flask, render_template
from models.data_point import DataPoint
import redis

app = Flask(__name__)
app.debug = True
app.db = None

@app.route('/')
def index():
    point = DataPoint(10, 10)
    return render_template('index.html', data_point=point.json())

if __name__ == '__main__':
    app.run()


def get_db():
    if app.db is None:
        app.db = redis.StrictRedis(host='localhost', port=6379, db=0)
    return app.db