from map_of_the_race import factory_method, commands_to_iterator

"""
    check out data structure module:
    update method needed to be a component of 
    data structure implementor 
    more precisely it must implement update method depending
    on "easy and hard game"!  
"""

# User will have a car and car will have map :
# map will be initialized after user's answers :
# choose complexity of a game


class Map:
    # I can define "abstract_factory"(i mean configure length and road type),
    # but instead i will offer differnt length of road

    def __init__(self, length, road_type):
        self.factory = factory_method.FactoryForCommands()
        self.base_class = commands_to_iterator.Commands
        self.updater_of_map = None
        self.road_type = road_type
        self.length = length
        self.iterator = None
        # {"Left" : None, "Middle" : None, "Right" : None}
        # by injecting iterator (abstract factory) data structure also will be cahnged!
        self.data_structure = None

    # think about self.road_type's data structure 
    def change_data_structure_state(self):
        self.data_structure = self.road_type.update_data_structure(self.data_structure)

    def set_iterator(self, new_iterator):
        self.iterator = new_iterator.give_me_iterator()
        self.data_structure = new_iterator.give_me_data_structure() 

    def set_map_updater(self, new_abstract_factory):
        updater = new_abstract_factory.update_the_state()
        self.updater_of_map = updater(self)

    def update_the_state(self, speed, side, wheel_type):
        # updater_of_map is already initialized  
        self.updater_of_map.update(speed, wheel_type)
        
        # side is needed to know what method of iterator to call!
        generated_item_from_iterator = self.factory.create(side, self.base_class, self.iterator) 
        
        return generated_item_from_iterator

    def set_data_structure(self, data_structure):
        self.data_structure = data_structure

    # True will be returned if it is an obsteacle!
    def is_obsteacle(self, decorator):
        return self.road_type.is_obsteacle(decorator)

    def return_road_type(self):
        return self.road_type.return_road_type()

    def show_what_is_going_on(self):
        representation = "Distance to finish: {}\n".format(self.length)
        representation += "You are know in {} side of road\n".format(self.iterator.give_me_current_road_side())
        # i have to update data structure state first then represent below description to user!

        for key in self.data_structure:
            if type(self.data_structure[key]) == int:
                representation += "{}: amount of points is {}\n".format(key, self.data_structure[key])

            else:
                representation += "{}: {}\n".format(key, self.data_structure[key].__str__())

        return representation            

    # To choose sth user have to know about "sth's" representation
    def __str__(self):
        representation = "Length of this road is {}\n".format(self.length)
        representation += "This map has {} sides of road\n".format(len(self.data_structure))
        representation += self.road_type.__str__()

        return representation