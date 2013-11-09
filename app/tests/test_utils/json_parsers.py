from flask import json


def extract_value_from_json(string, key):
    return json.loads(string)[key]