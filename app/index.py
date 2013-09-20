from flask import Flask, render_template
from models.data_point import DataPoint

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    point = DataPoint(10, 10)
    return render_template('index.html', data_point=point.json())

if __name__ == '__main__':
    app.run()
