class DataServer:

    def __init__(self):
        self.visualisations = []

    def add_visualisation(self, visualisation):
        visualisation.graph_id = self.next_visualisation_id()
        self.visualisations.append(visualisation)
        return visualisation.graph_id

    def find_max_visualisation_id(self):
        max_id = None
        for visualisation in self.visualisations:
            current_visualisation_id = visualisation.graph_id
            if current_visualisation_id > max_id:
                max_id = current_visualisation_id
        return max_id

    def next_visualisation_id(self):
        max_id = self.find_max_visualisation_id()
        if max_id is None:
            return 0
        return max_id + 1

    def add_data_point_to_visualisation(self, data_point, visualisation_id):
        visualisation = self.find_visualisation_by_id(visualisation_id)
        visualisation.add_data_point(data_point)

    def get_data_for_visualisation(self, visualisation_id):
        visualisation = self.find_visualisation_by_id(visualisation_id)
        return visualisation.get_data()

    def find_visualisation_by_id(self, visualisation_id):
        for visualisation in self.visualisations:
            if visualisation.graph_id == visualisation_id:
                return visualisation
        return None
