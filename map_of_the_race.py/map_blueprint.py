class Map:
    def __init__(self, length):
        self.type = None
        self.length = length
        self.updater_of_map = None
        self.data_structure = None 

    def set_map_updater(self, new_abstract_factory):
        self.updater_of_map = new_abstract_factory.update_the_state(self)

    def update_the_state(self, speed, wheel_type):
        self.updater_of_map.update(speed, wheel_type)