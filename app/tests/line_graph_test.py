from unittest import TestCase
from data_point import DataPoint
from line_graph import LineGraph


class LineGraphTest(TestCase):

    def test_should_accept_data_points(self):
        data_point = DataPoint(10, 10)
        graph = LineGraph()

        graph.add_data_point(data_point)

        returned_data_point = graph.get_data_point()

        self.assertEquals(returned_data_point, data_point)

    def test_should_get_oldest_data_point_first(self):
        first_data_point = DataPoint(10, 0)
        second_data_point = DataPoint(20, 10)
        graph = LineGraph()

        graph.add_data_point(first_data_point)
        graph.add_data_point(second_data_point)

        returned_data_point = graph.get_data_point()

        self.assertEquals(returned_data_point, first_data_point)