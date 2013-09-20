from Queue import Queue


class LineGraph:

    def __init__(self):
        self.__data = Queue()

    def add_data_point(self, data_point):
        self.__data.put(data_point)

    def get_data_point(self):
        return self.__data.get()

