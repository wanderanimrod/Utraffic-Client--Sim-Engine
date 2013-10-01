import app
from models.vehicle_snapshot import VehicleSnapshot

db = app.get_db()


def get_vehicle_snapshots(snapshot_ids):
    global db
    pipeline = db.pipeline()
    for snapshot_id in snapshot_ids:
        pipeline.hgetall(snapshot_id)
    vehicles_dict_list = pipeline.execute()
    vehicles = []
    for vehicle_dict in vehicles_dict_list:
        if vehicle_dict != {}:
            vehicles.append(VehicleSnapshot.make_from_dict(vehicle_dict))
    return vehicles