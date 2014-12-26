class VehicleSnapshot:

    def __init__(self, vehicle_id, timestamp):
        self.desired_velocity = 0.0
        self.velocity = 0.0
        self.acceleration = 0.0
        self.position = 0.0
        self.lane = 0
        self.vehicle_id = vehicle_id
        self.timestamp = timestamp
        self.id = self.__str__()

    def __eq__(self, other):
        return self.id == other.id

    @staticmethod
    def make_from_dict(vehicle_dict):
        vehicle_snapshot = VehicleSnapshot(vehicle_dict['id'], vehicle_dict['timestamp'])
        for key in vehicle_dict.keys():
            setattr(vehicle_snapshot, key, vehicle_dict[key])
        return vehicle_snapshot

    def __str__(self):
        return "vehicle:%s, timestamp:%s" % (self.vehicle_id, self.timestamp)
