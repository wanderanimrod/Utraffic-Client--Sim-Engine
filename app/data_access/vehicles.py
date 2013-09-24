import app
from models.vehicle import Vehicle

db = app.get_db()


def get_vehicle(vehicle_id):
    global db
    vehicle_dict = db.hgetall(vehicle_id)
    if vehicle_dict != {}:
        return Vehicle.make_from_dict(vehicle_dict)
    return None