import app

db = app.get_db()


def get_vehicle(vehicle_id):
    global db
    return db.hgetall(vehicle_id)