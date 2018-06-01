from map_of_the_race import factory_method

class Road:
    def __init__(self):
        self.road_type = None
        self.obsteacle = None

    # Data structure will be passed from map(map_blueprint.py module)
    def update_data_structure(self, data_structure):
        data_structure_implementor = factory_method.Factory().create(data_structure, self.obsteacle, self.road_type.points)
        
        return data_structure_implementor.update()

    def set_new_abstract_factory(self, road_supplier):
        # this is already initialized
        self.road_type = road_supplier.give_a_road_type()
        # this is still not initialized
        self.obsteacle = road_supplier.give_an_obsteacle()
    
    def is_obsteacle(self, decorator):
        return self.obsteacle.is_obsteacle(decorator)

    def retur_road_type(self):
        return self.road_type.road_type    
 
    def __str__(self):
        representataion = self.road_type.__str__()
        representataion += self.obsteacle.__str__()

        return representataion        
        
# import map_of_the_race.road_implementors.snippet_of_the_game        