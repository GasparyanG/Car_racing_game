class RoadType:
    def __init__(self, road_type, points):
        self.road_type = road_type
        self.points = points

    def __str__(self):
        representation = "This road type is {}\n".format(self.road_type)
        representation += "Max points that you can score in this map at once is {}\n".format(self.points)

        return representation