import app
from models.vehicle import Vehicle

db = app.get_db()


def get_vehicle(vehicle_id):
    global db
    vehicle_dict = db.hgetall(vehicle_id)
    if vehicle_dict != {}:
        return Vehicle.make_from_dict(vehicle_dict)
    return None


def get_vehicles(vehicle_ids):
    global db
    pipeline = db.pipeline()
    for vehicle_id in vehicle_ids:
        pipeline.hgetall(vehicle_id)
    vehicles_dict_list = pipeline.execute()
    vehicles = []
    for vehicle_dict in vehicles_dict_list:
        if vehicle_dict != {}:
            vehicles.append(Vehicle.make_from_dict(vehicle_dict))
    return vehicles