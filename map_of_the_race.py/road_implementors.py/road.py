import factory_method

class Road:
    def __init__(self):
        self.road_type = None
        self.data_structue = None
        self.obsteacle = None

    def update_data_structure(self):
        data_structure_implementor = factory_method.Factory().create(self.data_structue, self.obsteacle, self.road_type.points)
        
        return data_structure_implementor.update()

    def set_new_abstract_factory(self, road_supplier):
        # this is already initialized
        self.road_type = road_supplier.give_a_road_type()
        # this is still not initialized
        self.obsteacle = road_supplier.give_an_obsteacle()  
 
    def set_data_structure(self, new_data_structure):
        self.data_structue = new_data_structure    