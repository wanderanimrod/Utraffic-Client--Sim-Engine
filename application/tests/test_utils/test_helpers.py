from application.models.data_point import DataPoint
from application.models.series import Series
from application.models.vehicle_snapshot import VehicleSnapshot


def make_data_point():
    return DataPoint(10, 10)


def make_series(series_id=0):
    return Series(series_id=series_id)


def make_two_different_data_points():
    return [DataPoint(10, 0), DataPoint(20, 10)]


def make_series_with_two_different_data_points():
        series = make_series()
        data_points = make_two_different_data_points()
        for data_point in data_points:
            series.add_data_point(data_point)
        return series, data_points


def make_fully_constituted_vehicle_snapshot(vehicle_id=1, timestamp=0):
    snapshot = VehicleSnapshot(vehicle_id, timestamp)
    snapshot.acceleration = 10.0
    snapshot.velocity = 50.0
    snapshot.lane = 0
    snapshot.position = 150.0
    snapshot.desired_velocity = 60
    return snapshot