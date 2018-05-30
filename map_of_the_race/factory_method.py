# import data_sturcture_implementor
from map_of_the_race import road_implementors 

class Factory:
    def __init__(self):
        self.base_data_structure = road_implementors.data_structure_implementor.DataStructureImplementor
    
    def create(self, data_structure, obsteacle, points):
        products = self.products_to_be_created()

        for product in products:
            product = product(data_structure, obsteacle, points)
            if product.is_used():
                return product

    def products_to_be_created(self):
        products = self.base_data_structure.__subclasses__()

        return products