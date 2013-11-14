from tests.test_utils.json_parsers import extract_value_from_json


def create_new_series(app, with_dummy_data=False):
    if with_dummy_data:
        post = app.post('/series/?debug=true')
    else:
        post = app.post('/series/')
    return extract_value_from_json(post.data, 'id'), post