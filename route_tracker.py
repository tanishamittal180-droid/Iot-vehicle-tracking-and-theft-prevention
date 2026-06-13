class RouteTracker:
    
    def __init__(self):

        self.points = []

    def add_point(
            self,
            lat,
            lon):

        self.points.append(
            (lat, lon)
        )

    def total_points(self):

        return len(
            self.points
        )

    def get_route(self):

        return self.points