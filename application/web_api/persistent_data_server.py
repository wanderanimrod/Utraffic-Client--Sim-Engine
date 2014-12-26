from application.models.data_server import DataServer

data_server = None


def get_data_server():
    global data_server
    if data_server is None:
        data_server = DataServer()
    return data_server