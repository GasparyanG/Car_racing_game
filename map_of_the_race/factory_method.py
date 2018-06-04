# import data_sturcture_implementor
from map_of_the_race.road_implementors import data_structure_implementor

class Factory:
    def __init__(self):
        self.base_data_structure = data_structure_implementor.DataStructureImplementor
    
    def create(self, data_structure, obsteacle, points):
        products = self.products_to_be_created()

        for product in products:
            product = product(data_structure, obsteacle, points)
            if product.is_used():
                return product

    def products_to_be_created(self):
        products = self.base_data_structure.__subclasses__()

        return products


class FactoryForCommands:
    def create(self, comparable_object, base_class, iterator):
        products = self.products_to_be_created(base_class)

        for product in products:
            product = product(iterator)
            if product.is_used(comparable_object):
                return product

    def products_to_be_created(self, base_class):
        products = base_class.__subclasses__()

        return products