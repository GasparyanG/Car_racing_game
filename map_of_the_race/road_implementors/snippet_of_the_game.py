from map_of_the_race.road_implementors import road_suppliers, factory_method, road
from map_of_the_race import map_blueprint 

class SnippetOfTheGame:
    def __init__(self):
        self.road_suppliers_base_class = road_suppliers.RoadSuppliers
        self.factory = factory_method.Factory()
        self.map_road = road.Road()
        self.map = map_blueprint.Map

    def start(self):
        is_handled = True
        while is_handled:
            """
                I have to offer road suppliers
                which will be injected into Road class
                after which i have to instansiate map by injecting
                length and road_type (i.e. above mentioned Road class which after 
                injection will be initialized) 
            """    
            
            representation = self.representaion_of_road_types()
            print(representation)

            comparable_object = input("Choose road type by typing corresponding number: ")

            supplier_of_road = self.factory.create(comparable_object, self.road_suppliers_base_class)

            if supplier_of_road == None:
                continue
            self.map_road.set_new_abstract_factory(supplier_of_road)
            
            while True:
                info = self.offering_road_length()
                
                print(info[0])
                choice = input("Choose road length by typing correspoinding number: ")

                length = self.is_valid(choice, info[1])   
                if length == False:
                    continue

                self.map = self.map(length, self.map_road)    
                
                return self.map

    def is_valid(self, choice, length_of_road):
        list_of_numbers = []
        for number in range(len(length_of_road)):
            list_of_numbers.append(number + 1)
        
        try:
            choice = int(choice)
            if choice in list_of_numbers:
                return choice
        except ValueError:
            return False     

    def representaion_of_road_types(self):
        list_of_road_types = self.road_suppliers_base_class.__subclasses__()

        representation = ""
        for index, road_type in enumerate(list_of_road_types):
            representation += "{}){}\n".format(index + 1, road_type().__str__())

        return representation     

    def offering_road_length(self):
        length_of_road = [500, 2000, 5000]
 
        road_length_offer = ""
        for index, length in enumerate(length_of_road):
            road_length_offer += "{}){}\n".format(index + 1, length)
            
        return [road_length_offer, length_of_road]