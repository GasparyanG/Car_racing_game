from map_of_the_race.abstract_factory import ConfigurationOfDictionary
# updater and notifier of observable pattern needed to be
# configured in this scenario
from configured_implementors import abstract_factory
# this will be offered for choice 
from map_of_the_race.road_implementors import road_suppliers, road, factory_method
# user's car need to have map for race!
from map_of_the_race import map_blueprint


class MapCreator:
    def __init__(self):
        self.suppliers = road_suppliers.RoadSuppliers
        self.road_type = road.Road()
        self.map = map_blueprint.Map

    def define_users_cars_map(self, user):
        raise NotImplementedError()

    def represent_lengths_of_road(self):
        list_of_lengths = [500, 1000, 2000]

        representation = ""
        for index, length in enumerate(list_of_lengths):
            representation += "{}){}\n".format(index + 1, length)

        while True:
            print(representation)
            user_choice_of_length = input("Choose road length by typing corresponding number: ")
            
            user_choice_of_length = self.is_valid(user_choice_of_length, list_of_lengths)
            if not user_choice_of_length:
                print("Don't violate the requirements!")
                continue 

            desired_length = list_of_lengths[user_choice_of_length - 1]
            
            return desired_length
        
    def is_valid(self, user_choice, list_data_type):
        list_of_numbers = []

        for number in range(len(list_data_type)):
            list_of_numbers.append(number + 1)

        try:
            user_choice = int(user_choice)
            if user_choice in list_of_numbers:
                return user_choice

        except ValueError:
            return False        

    def representaion_of_road_suppliers(self):
        subclasses = self.suppliers.__subclasses__()

        list_of_objects = []
        representation = ""
        for index, subclass in enumerate(subclasses):
            subclass = subclass()
            representation += "{}){}".format(index + 1, subclass.__str__())
            list_of_objects.append(subclass)

        while True:
            print(representation)
            user_choice = input("Choose road type by typing corresponding number: ")
 
            user_choice = self.is_valid(user_choice, list_of_objects)
            if not user_choice:
                print("Don't violate the requirements!")
                continue

            desired_configuration = list_of_objects[user_choice - 1]

            self.road_type.set_new_abstract_factory(desired_configuration)

            return self.road_type


class MapCreatorForEasyGame(MapCreator):
    def __init__(self):
        super().__init__()
        self.easy_game = abstract_factory.EasyGame()
        # here i have to have iterator and data structure holding abstract factroy
        self.configuration = ConfigurationOfDictionary

    def define_users_cars_map(self, user):
        arguments_for_other_cars = [] 
        # arguments_for_other_cars.append(self.easy_game)

        desired_length = self.represent_lengths_of_road()
        arguments_for_other_cars.append(desired_length)

        road_type = self.representaion_of_road_suppliers()
        arguments_for_other_cars.append(road_type)

        defined_map = self.map(desired_length, road_type)
        defined_map.set_map_updater(self.easy_game)

        defined_map.set_iterator(self.configuration())

        # others need to have own iterator
        iteratort_for_others = self.configuration
        arguments_for_other_cars.append(iteratort_for_others)

        # iterator of cars' map is missing!
        
        user.change_cars_map(defined_map)
        user.change_cars_notifier(self.easy_game)

        return arguments_for_other_cars