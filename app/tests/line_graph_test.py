from unittest import TestCase
from data_point import DataPoint
from line_graph import LineGraph


class LineGraphTest(TestCase):

    def setUp(self):
        self.graph = LineGraph()

    def test_should_accept_data_points(self):
        data_point = self.make_data_point()

        self.graph.add_data_point(data_point)

        returned_data_point = self.graph.get_data_point()

        self.assertEquals(returned_data_point, data_point)

    def test_should_get_oldest_data_point_first(self):
        first_data_point, second_data_point = self.make_two_data_points()

        self.graph.add_data_point(first_data_point)
        self.graph.add_data_point(second_data_point)

        returned_data_point = self.graph.get_data_point()

        self.assertEquals(returned_data_point, first_data_point)

    def test_get_data_point_should_return_none_on_if_graph_has_no_data(self):
        returned_data_point = self.graph.get_data_point()
        self.assertEquals(returned_data_point, None)

    def test_should_remove_data_point_after_get_data_point(self):
        self.graph.add_data_point(self.make_data_point())
        self.graph.get_data_point()
        next_data_point = self.graph.get_data_point()
        self.assertIsNone(next_data_point)

    def make_two_data_points(self):
        return DataPoint(10, 0), DataPoint(20, 10)

    def make_data_point(self):
        return DataPoint(10, 10)