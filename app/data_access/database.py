from app import app
import redis


def get_db():
    if app.db is None:
        app.db = redis.StrictRedis(host='localhost', port=6379, db=0)
    return app.db