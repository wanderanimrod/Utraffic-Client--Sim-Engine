from unittest import TestCase
from tests.test_utils.test_helpers import make_fully_constituted_vehicle_snapshot
from models.vehicle_snapshot import VehicleSnapshot


class VehicleSnapshotTest(TestCase):

    def test_should_convert_itself_to_dictionary_with_all_fields_included_and_values_correctly_matched(self):
        snapshot = make_fully_constituted_vehicle_snapshot()
        snapshot_dict = snapshot.__dict__
        expected_dict = {'acceleration': 10.0, 'desired_velocity': 60, 'id': 'vehicle:1, timestamp:0',
                         'lane': 0, 'position': 150.0, 'velocity': 50, 'vehicle_id': 1, 'timestamp': 0}
        self.assertEquals(snapshot_dict, expected_dict)

    def test_should_equate_two_vehicle_snapshots_with_the_same_id_and_timestamp(self):
        same_id = 'same_vehicle_id'
        same_timestamp = 0
        snapshot_one = make_fully_constituted_vehicle_snapshot(vehicle_id=same_id, timestamp=same_timestamp)
        snapshot_two = make_fully_constituted_vehicle_snapshot(vehicle_id=same_id, timestamp=same_timestamp)
        self.assertEquals(snapshot_one, snapshot_two)

    def test_should_not_equate_two_vehicle_snapshots_with_different_vehicle_ids_but_same_timestamps(self):
        same_timestamp = 0
        snapshot_one = make_fully_constituted_vehicle_snapshot(vehicle_id="id_1", timestamp=same_timestamp)
        snapshot_two = make_fully_constituted_vehicle_snapshot(vehicle_id="id_2", timestamp=same_timestamp)
        self.assertNotEquals(snapshot_one, snapshot_two)

    def test_should_not_equate_two_vehicle_snapshots_with_same_vehicle_ids_but_different_timestamps(self):
        same_id = "id"
        snapshot_one = make_fully_constituted_vehicle_snapshot(vehicle_id=same_id, timestamp=0)
        snapshot_two = make_fully_constituted_vehicle_snapshot(vehicle_id=same_id, timestamp=10)
        self.assertNotEquals(snapshot_one, snapshot_two)

    def test_should_convert_valid_dict_into_valid_vehicle_snapshot(self):
        snapshot_dict = {'acceleration': 10.0, 'desired_velocity': 60,
                         'lane': 0, 'position': 150.0, 'velocity': 50, 'id': 1, 'timestamp': 10}
        constructed_snapshot = VehicleSnapshot.make_from_dict(snapshot_dict)
        self.assertTrue(self.vehicle_snapshot_has_all_fields_and_values_in_dict(constructed_snapshot, snapshot_dict))

    def test_vehicle_snapshot_string_representation_should_contain_both_the_vehicle_id_and_timestamp(self):
        vehicle_id = 100
        timestamp = 10
        snapshot = make_fully_constituted_vehicle_snapshot(vehicle_id=vehicle_id, timestamp=timestamp)
        stringified_snapshot = snapshot.__str__()
        expected_string = "vehicle:%d, timestamp:%d" % (vehicle_id, timestamp)
        self.assertEquals(stringified_snapshot, expected_string)

    def test_vehicle_snapshot_id_should_be_the_string_representation_of_the_object(self):
        snapshot = make_fully_constituted_vehicle_snapshot(vehicle_id=1, timestamp=10)
        expected_id = 'vehicle:1, timestamp:10'
        self.assertEquals(snapshot.id, expected_id)

    @staticmethod
    def vehicle_snapshot_has_all_fields_and_values_in_dict(constructed_snapshot, snapshot_dict):
        for key in snapshot_dict.keys():
            if getattr(constructed_snapshot, key) != snapshot_dict[key]:
                return False
        return True