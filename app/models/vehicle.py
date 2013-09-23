class Vehicle:

    def __init__(self, vehicle_id, desired_velocity):
        self.velocity = 0.0
        self.acceleration = 0.0
        self.position = 0.0
        self.lane = 0
        self.id = vehicle_id
        self.desired_velocity = desired_velocity

    def __eq__(self, other):
        if other.id == self.id:
            return True
        return False

    @staticmethod
    def make_from_dict(vehicle_dict):
        pass