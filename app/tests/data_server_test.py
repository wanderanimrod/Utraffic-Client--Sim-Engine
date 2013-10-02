from unittest import TestCase
from mock import Mock
from models.data_server import DataServer
from tests import test_helpers


class DataServerTest(TestCase):

    def setUp(self):
        self.data_server = DataServer()

    def test_should_assign_id_to_every_visualisation_added(self):
        line_graph = test_helpers.make_line_graph()
        graph_id = self.data_server.add_visualisation(line_graph)
        self.assertIsNotNone(graph_id)

    def test_next_visualisation_id_should_be_1_greater_than_current_maximum_id(self):
        data_server = self.make_data_server_with_two_visualisations()
        data_server.find_max_visualisation_id = Mock(return_value=10)
        next_id = data_server.next_visualisation_id()
        self.assertEquals(next_id, 11)

    def test_should_find_highest_visualisation_among_ids_currently_assigned(self):
        data_server = self.make_data_server_with_two_visualisations()
        highest_id = data_server.find_max_visualisation_id()
        expected_highest_id = 1
        self.assertEquals(highest_id, expected_highest_id)

    def test_should_find_visualisation_by_id(self):
        data_server, visualisation = self.make_data_server_with_one_visualisation()
        returned_visualisation = data_server.find_visualisation_by_id(visualisation.graph_id)
        self.assertEquals(returned_visualisation, visualisation)

    def test_should_return_none_if_visualisation_with_specified_id_does_not_exist(self):
        data_server, visualisation = self.make_data_server_with_one_visualisation()
        non_existent_visualisation_id = visualisation.graph_id + 100
        returned_visualisation = data_server.find_visualisation_by_id(non_existent_visualisation_id)
        self.assertIsNone(returned_visualisation)

    def test_should_serve_all_data_currently_in_a_specified_line_graph(self):
        visualisation, expected_data = test_helpers.make_graph_with_two_different_data_points()
        data_server, _ = self.make_data_server_with_one_visualisation(visualisation=visualisation)
        returned_data = data_server.get_data_for_visualisation(visualisation.graph_id)
        self.assertEquals(returned_data, expected_data)

    def test_should_add_data_point_to_a_specified_line_graph(self):
        data_point = test_helpers.make_data_point()
        data_server, visualisation = self.make_data_server_with_one_visualisation()
        visualisation_id = visualisation.graph_id
        data_server.add_data_point_to_visualisation(data_point, visualisation_id)
        returned_visualisation_data = data_server.get_data_for_visualisation(visualisation_id)
        self.assertTrue(data_point in returned_visualisation_data)

    def make_data_server_with_two_visualisations(self):
        first_visualisation = test_helpers.make_line_graph()
        second_visualisation = test_helpers.make_line_graph()
        self.data_server.add_visualisation(first_visualisation)
        self.data_server.add_visualisation(second_visualisation)
        return self.data_server

    def make_data_server_with_one_visualisation(self, visualisation=test_helpers.make_line_graph()):
        self.data_server.add_visualisation(visualisation)
        return self.data_server, visualisation
