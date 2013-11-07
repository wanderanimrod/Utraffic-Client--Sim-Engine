from unittest import TestCase
from mock import Mock
from models.data_server import DataServer
from tests import test_helpers


class DataServerTest(TestCase):

    def setUp(self):
        self.data_server = DataServer()

    def test_should_assign_id_to_every_series_added(self):
        line_graph = test_helpers.make_series()
        graph_id = self.data_server.add_series(line_graph)
        self.assertIsNotNone(graph_id)

    def test_next_series_id_should_be_1_greater_than_current_maximum_id(self):
        data_server = self.make_data_server_with_two_series()
        data_server.find_max_series_id = Mock(return_value=10)
        next_id = data_server.next_series_id()
        self.assertEquals(next_id, 11)

    def test_should_find_highest_series_id_among_ids_currently_assigned(self):
        data_server = self.make_data_server_with_two_series()
        highest_id = data_server.find_max_series_id()
        expected_highest_id = 1
        self.assertEquals(highest_id, expected_highest_id)

    def test_should_find_series_by_id(self):
        data_server, series = self.make_data_server_with_one_series()
        returned_series = data_server.find_series_by_id(series.graph_id)
        self.assertEquals(returned_series, series)

    def test_should_return_none_if_series_with_specified_id_does_not_exist(self):
        data_server, series = self.make_data_server_with_one_series()
        non_existent_series_id = series.series_id - 100
        returned_series = data_server.find_series_by_id(non_existent_series_id)
        self.assertIsNone(returned_series)

    def test_should_serve_all_data_currently_in_a_specified_series(self):
        series, expected_data = test_helpers.make_series_with_two_different_data_points()
        data_server, _ = self.make_data_server_with_one_series(series=series)
        returned_data = data_server.get_data_for_series(series.series_id)
        self.assertEquals(returned_data, expected_data)

    def test_should_add_data_point_to_a_specified_series(self):
        data_point = test_helpers.make_data_point()
        data_server, series = self.make_data_server_with_one_series()
        series_id = series.series_id
        data_server.add_data_point_to_series(data_point, series_id)
        returned_series_data = data_server.get_data_for_series(series_id)
        self.assertTrue(data_point in returned_series_data)

    def make_data_server_with_two_series(self):
        first_series = test_helpers.make_series()
        second_series = test_helpers.make_series()
        self.data_server.add_series(first_series)
        self.data_server.add_series(second_series)
        return self.data_server

    def make_data_server_with_one_series(self, series=test_helpers.make_series()):
        self.data_server.add_series(series)
        return self.data_server, series
