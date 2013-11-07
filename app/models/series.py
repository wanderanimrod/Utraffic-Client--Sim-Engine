from Queue import Queue, Empty


class Series:

    def __init__(self, series_id=0):
        self.series_id = series_id
        self.__data = Queue()

    def add_data_point(self, data_point):
        self.__data.put(data_point)

    def get_data_point(self):
        try:
            return self.__data.get_nowait()
        except Empty:
            return None

    def get_data(self):
        data = []
        while not self.__data.empty():
            data.append(self.get_data_point())
        return data