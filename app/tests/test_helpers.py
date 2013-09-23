from models.line_graph import LineGraph
from models.data_point import DataPoint
from models.vehicle import Vehicle


def make_data_point():
    return DataPoint(10, 10)


def make_line_graph(graph_id=0):
    return LineGraph(graph_id=graph_id)


def make_two_different_data_points():
    return [DataPoint(10, 0), DataPoint(20, 10)]


def make_graph_with_two_different_data_points():
        graph = make_line_graph()
        data_points = make_two_different_data_points()
        for data_point in data_points:
            graph.add_data_point(data_point)
        return graph, data_points


def make_fully_constituted_vehicle(vehicle_id=1):
    vehicle = Vehicle(vehicle_id, 60)
    vehicle.acceleration = 10.0
    vehicle.velocity = 50.0
    vehicle.lane = 0
    vehicle.position = 150.0
    return vehicle