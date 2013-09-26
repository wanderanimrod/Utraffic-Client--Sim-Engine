from unittest import TestCase
from data_access import settings
from data_access.vehicles import get_vehicles
import redis
from tests.test_helpers import make_fully_constituted_vehicle


class VehiclesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = redis.StrictRedis(host=settings.host, port=settings.port, db=0)

    def test_get_vehicles_should_get_multiple_vehicles_from_the_db_by_id(self):
        vehicle_one = make_fully_constituted_vehicle(vehicle_id="vehicle:1")
        vehicle_two = make_fully_constituted_vehicle(vehicle_id="vehicle:2")
        for vehicle in [vehicle_one, vehicle_two]:
            self.db_insert_vehicle(vehicle_id=vehicle.id)
        returned_vehicles = get_vehicles([vehicle_one.id, vehicle_two.id])
        self.assertEquals(returned_vehicles, [vehicle_one, vehicle_two])

    def test_get_vehicles_should_return_empty_list_if_no_vehicles_with_specified_ids_exist_in_the_db(self):
        self.assertEquals(get_vehicles(["NON_EXISTENT_ID_1", "NON_EXISTENT_ID_2"]), [])

    def test_get_vehicles_should_delete_all_returned_vehicles_from_db(self):
        pass

    def db_insert_vehicle(self, vehicle_id='test_vehicle'):
        vehicle = make_fully_constituted_vehicle(vehicle_id=vehicle_id)
        vehicle_dict = vehicle.__dict__
        self.db.hmset(vehicle_id, vehicle_dict)
        return vehicle