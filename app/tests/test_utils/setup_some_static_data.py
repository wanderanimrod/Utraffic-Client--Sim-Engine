from models.data_point import DataPoint


def fill_series_with_static_data(data_server, series_id):
    for i in range(0, 11):
        data_point = DataPoint(i, i)
        data_server.add_data_point_to_series(data_point, series_id)