from flask import json


def extract_value_from_json(string, key):
    return json.loads(string)[key]


def json_string_has_expected_keys(string, expected_keys):
    jsonified_string = json.loads(string)
    for key in expected_keys:
        if key not in jsonified_string:
            return False
    return True