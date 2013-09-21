from unittest import TestCase
from models.line_graph import LineGraph
from tests import test_helpers


class LineGraphTest(TestCase):

    def setUp(self):
        self.graph = test_helpers.make_line_graph()

    def test_should_accept_data_points(self):
        data_point = test_helpers.make_data_point()
        self.graph.add_data_point(data_point)
        returned_data_point = self.graph.get_data_point()
        self.assertEquals(returned_data_point, data_point)

    def test_should_get_oldest_data_point_first(self):
        first_data_point, second_data_point = test_helpers.make_two_different_data_points()
        self.graph.add_data_point(first_data_point)
        self.graph.add_data_point(second_data_point)
        returned_data_point = self.graph.get_data_point()
        self.assertEquals(returned_data_point, first_data_point)

    def test_get_data_point_should_return_none_on_if_graph_has_no_data(self):
        returned_data_point = self.graph.get_data_point()
        self.assertIsNone(returned_data_point)

    def test_should_remove_data_point_after_get_data_point(self):
        graph = self.make_graph_with_one_data_point()
        graph.get_data_point()
        next_data_point = graph.get_data_point()
        self.assertIsNone(next_data_point)

    def test_should_get_all_data_points(self):
        graph, data_points = test_helpers.make_graph_with_two_different_data_points()
        returned_data_points = graph.get_data()
        self.assertEquals(returned_data_points, data_points)

    def test_getting_all_data_points_should_leave_no_data(self):
        graph, _ = test_helpers.make_graph_with_two_different_data_points()
        graph.get_data()
        next_data_point = graph.get_data_point()
        self.assertIsNone(next_data_point)

    def test_should_have_an_id_of_zero_by_default(self):
        graph = LineGraph()
        graph_id = graph.graph_id
        self.assertEquals(graph_id, 0)

    def make_graph_with_one_data_point(self):
        data_point = test_helpers.make_data_point()
        self.graph.add_data_point(data_point)
        return self.graph
