from models.data_point import DataPoint
from models.series import series_status


def make_static_data_points():
    data_points = []
    for i in range(0, 11):
        data_points.append(DataPoint(i, i))
    return data_points


def fill_series_with_static_data(data_server, series_id):
    data_points = make_static_data_points()
    for data_point in data_points:
        data_server.add_data_point_to_series(data_point, series_id)
    series = data_server.get_series(series_id)
    series.status = series_status.COMPLETE