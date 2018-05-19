import obsteacle, types_of_road

class RoadSuppliers:
    def give_an_obsteacle(self):
        raise NotImplementedError()

    def give_a_road_type(self):
        raise NotImplementedError()


class WinterRoadSuppliers(RoadSuppliers):
    def give_an_obsteacle(self):
        return obsteacle.WinterObsteacle
    
    def give_a_road_type(self):
        return types_of_road.RoadType("Winter", 30)


class AutumnRoadSuppliers(RoadSuppliers):
    def give_an_obsteacle(self):
        return obsteacle.AutumnObsteacle

    def give_a_road_type(self):
        return types_of_road.RoadType("Autumn", 25)        