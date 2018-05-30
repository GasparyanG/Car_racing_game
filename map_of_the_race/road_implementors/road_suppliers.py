from map_of_the_race.road_implementors import obsteacle, types_of_road

""" 
    user will be ask about road type :
        choose road type (prompt will give importatnt
        information about road) by typing correspoinding number!
"""


class RoadSuppliers:
    def is_used(self, comparable_object):
        raise NotImplementedError()

    def give_an_obsteacle(self):
        raise NotImplementedError()

    def give_a_road_type(self):
        raise NotImplementedError()

    def __str__(self):
        representation = self.give_a_road_type().__str__()

        return representation


class WinterRoadSuppliers(RoadSuppliers):
    def is_used(self, comparable_object):
        return comparable_object == "1"

    def give_an_obsteacle(self):
        return obsteacle.WinterObsteacle()
    
    def give_a_road_type(self):
        return types_of_road.RoadType("Winter", 30)


class AutumnRoadSuppliers(RoadSuppliers):
    def is_used(self, comparable_object):
        return comparable_object == "2"

    def give_an_obsteacle(self):
        return obsteacle.AutumnObsteacle()

    def give_a_road_type(self):
        return types_of_road.RoadType("Autumn", 25)        