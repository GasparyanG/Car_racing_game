"""
    check out data structure module :
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
        self.updater_of_map = None
        self.road_type = road_type
        self.length = length
        self.data_structure = {"Left" : None, "Middle" : None, "Right" : None} 

    # think about self.road_type's data structure 
    def change_data_structure_state(self):
        self.data_structure = self.road_type.update_data_structure(self.data_structure)

    def set_map_updater(self, new_abstract_factory):
        self.updater_of_map = new_abstract_factory.update_the_state(self)

    def update_the_state(self, speed, wheel_type):
        self.updater_of_map.update(speed, wheel_type)

    def set_data_structure(self, data_structure):
        self.data_structure = data_structure

    # To choose sth user have to know about "sth's" representation
    def __str__(self):
        representation = "Length of this road is {}\n".format(self.length)
        representation += "This map has {} sides of road\n".format(len(self.data_structure))
        representation += self.road_type.__str__()

        return representation               