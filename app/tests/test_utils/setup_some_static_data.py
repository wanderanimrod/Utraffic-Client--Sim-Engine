from models.data_point import DataPoint
from models.data_server import DataServer
from models.line_graph import LineGraph


def get_data_server():
    data_server = DataServer()
    line_graph = LineGraph()
    graph_id = data_server.add_visualisation(line_graph)

    for i in range(0, 11):
        data_point = DataPoint(i, i)
        data_server.add_data_point_to_visualisation(data_point, graph_id)

    return data_server