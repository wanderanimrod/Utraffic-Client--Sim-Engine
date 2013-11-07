class DataServer:

    def __init__(self):
        self.series = []

    def add_series(self, series):
        series.graph_id = self.next_series_id()
        self.series.append(series)
        return series.graph_id

    def find_max_series_id(self):
        max_id = None
        for series in self.series:
            current_series_id = series.graph_id
            if current_series_id > max_id:
                max_id = current_series_id
        return max_id

    def next_series_id(self):
        max_id = self.find_max_series_id()
        if max_id is None:
            return 0
        return max_id + 1

    def add_data_point_to_series(self, data_point, series_id):
        series = self.find_series_by_id(series_id)
        series.add_data_point(data_point)

    def get_data_for_series(self, series_id):
        series = self.find_series_by_id(series_id)
        return series.get_data()

    def find_series_by_id(self, series_id):
        for series in self.series:
            if series.graph_id == series_id:
                return series
        return None
