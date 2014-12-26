from unittest import TestCase
from application.data_access import settings
from application.data_access.vehicles import get_vehicle_snapshots
from application.tests.test_utils.test_helpers import make_fully_constituted_vehicle_snapshot

import redis


class VehiclesTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = redis.StrictRedis(host=settings.host, port=settings.port, db=0)

    def test_get_vehicle_snapshots_should_get_multiple_vehicle_snapshots_from_the_db_by_id(self):
        snapshot_one, snapshot_two = self.insert_two_vehicle_snapshots()
        returned_vehicle_snapshots = get_vehicle_snapshots([snapshot_one.id, snapshot_two.id])
        self.assertEquals(returned_vehicle_snapshots, [snapshot_one, snapshot_two])

    def test_get_vehicles_should_return_empty_list_if_no_vehicles_with_specified_ids_exist_in_the_db(self):
        self.assertEquals(get_vehicle_snapshots(["NON_EXISTENT_ID_1", "NON_EXISTENT_ID_2"]), [])

    def test_get_vehicles_should_delete_all_returned_vehicles_from_db(self):
        vehicle_snapshots = self.insert_two_vehicle_snapshots()
        get_vehicle_snapshots(list(vehicle_snapshots))
        snapshots_left_after_getting_snapshots = get_vehicle_snapshots(list(vehicle_snapshots))
        self.assertEquals(snapshots_left_after_getting_snapshots, [])

    def db_insert_vehicle_snapshot(self, vehicle_snapshot):
        snapshot = make_fully_constituted_vehicle_snapshot(vehicle_id=vehicle_snapshot.vehicle_id,
                                                           timestamp=vehicle_snapshot.timestamp)
        snapshot_dict = snapshot.__dict__
        self.db.hmset(snapshot.id, snapshot_dict)
        return snapshot

    def insert_two_vehicle_snapshots(self):
        snapshot_one = make_fully_constituted_vehicle_snapshot(vehicle_id=1, timestamp=0)
        snapshot_two = make_fully_constituted_vehicle_snapshot(vehicle_id=2, timestamp=0)
        for snapshot in [snapshot_one, snapshot_two]:
            self.db_insert_vehicle_snapshot(snapshot)
        return snapshot_one, snapshot_two