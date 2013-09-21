class DataPoint:

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def json(self):
        return {'value': self.value, 'time': self.time}

    def __str__(self):
        return str(self.json())