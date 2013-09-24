from unittest import TestCase
from data_access import settings
from data_access.vehicles import get_vehicle
import redis
from tests.test_helpers import make_fully_constituted_vehicle


class VehiclesTest(TestCase):

    def setUp(self):
        db_host_name = settings.host
        db_port = settings.port
        self.db = redis.StrictRedis(host=db_host_name, port=db_port, db=0)

    def test_should_get_vehicle_by_id_from_redis_hash_map(self):
        vehicle = self.db_insert_vehicle()
        returned_vehicle = get_vehicle(vehicle.id)
        self.assertEquals(returned_vehicle, vehicle)

    def test_should_return_none_if_vehicle_with_specified_id_does_not_exist_in_the_db(self):
        self.assertIsNone(get_vehicle("NON_EXISTENT_ID"))

    def db_insert_vehicle(self, vehicle_id='test_vehicle'):
        vehicle = make_fully_constituted_vehicle(vehicle_id=vehicle_id)
        vehicle_dict = vehicle.__dict__
        self.db.hmset(vehicle_id, vehicle_dict)
        return vehicle

