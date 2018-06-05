from random import shuffle, choice
import default_car_for_beginners
from map_of_the_race import map_blueprint
from configured_implementors import abstract_factory


class Bot:
    def __init__(self):
        self.bot_cars = []
        self.list_of_names = ["Rocket", "Flesh", "Turbo", "Lightning McQueen", "Schumacher"]  

    def random_name_creation(self, amount_of_names):
        list_of_random_names = []
        list_of_numbers = []
        positive_result_cycle = 0

        for number in range(amount_of_names):
            list_of_numbers.append(number)

        shuffle(list_of_numbers)    

        while positive_result_cycle < amount_of_names:
            random_name = "{}".format(choice(self.list_of_names)) + "{}".format(choice(list_of_numbers))
            
            if random_name not in list_of_random_names:
                list_of_random_names.append(random_name)
                positive_result_cycle += 1

        return list_of_random_names        
          
    def create_bots(self, amount, arg):
        raise NotImplementedError()


class BotsForEasyGame(Bot):
    def __init__(self):
        super().__init__()
        self.default_car_creator = default_car_for_beginners.CarForBeginners()
        self.map = map_blueprint.Map
        self.easy_game = abstract_factory.EasyGame()

    # road_type holds abstract factory's place!
    # length_of_road, road_type, configuration_of_iterator_and_data_structure
    def create_bots(self, amount, data_structure):
        length_of_road = data_structure[0]
        road_type = data_structure[1]
        configuration_of_iterator_and_data_structure = data_structure[2]

        list_of_random_names = self.random_name_creation(amount)

        # amount will be checked and then passed!
        for times in range(amount):
            default_car = self.default_car_creator.give_me_car()

            self.bot_cars.append(default_car)

        for bot_car in self.bot_cars:
            defined_map = self.define_map(length_of_road, road_type, configuration_of_iterator_and_data_structure)    

            updater = self.easy_game.update_the_state()
            notifier = self.easy_game.notify_about_changes()

            defined_map.set_map_updater(updater)
            bot_car.set_notifier(notifier)

            bot_car.set_map(defined_map)

        for index, bot_car in enumerate(self.bot_cars):
            bot_car.name = list_of_random_names[index]

        return self.bot_cars    

    def define_map(self, length_of_road, road_type, configuration_of_iterator_and_data_structure):
        defined_map = self.map(length_of_road, road_type)

        defined_map.set_iterator(configuration_of_iterator_and_data_structure)

        return defined_map