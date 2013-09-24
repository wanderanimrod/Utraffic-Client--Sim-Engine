from unittest import TestCase
from tests.test_helpers import make_fully_constituted_vehicle
from models.vehicle import Vehicle


class VehicleTest(TestCase):

    def test_should_convert_itself_to_dictionary_with_all_fields_included_and_values_correctly_matched(self):
        vehicle = make_fully_constituted_vehicle()
        vehicle_dict = vehicle.__dict__
        expected_dict = {'acceleration': 10.0, 'desired_velocity': 60,
                         'lane': 0, 'position': 150.0, 'velocity': 50, 'id': 1}
        self.assertEquals(vehicle_dict, expected_dict)

    def test_should_equate_two_vehicles_with_the_same_id(self):
        same_id = 'same_vehicle_id'
        vehicle_one = make_fully_constituted_vehicle(vehicle_id=same_id)
        vehicle_two = make_fully_constituted_vehicle(vehicle_id=same_id)
        self.assertEquals(vehicle_one, vehicle_two)

    def test_should_convert_valid_dict_into_valid_vehicle(self):
        vehicle_dict = {'acceleration': 10.0, 'desired_velocity': 60,
                        'lane': 0, 'position': 150.0, 'velocity': 50, 'id': 1}
        constructed_vehicle = Vehicle.make_from_dict(vehicle_dict)
        self.assertTrue(self.vehicle_has_all_fields_and_values_in_dict(constructed_vehicle, vehicle_dict))

    def vehicle_has_all_fields_and_values_in_dict(self, constructed_vehicle, vehicle_dict):
        for key in vehicle_dict.keys():
            if getattr(constructed_vehicle, key) != vehicle_dict[key]:
                return False
        return True

