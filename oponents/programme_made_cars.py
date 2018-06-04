import default_car_for_beginners
from map_of_the_race import map_blueprint
from configured_implementors import abstract_factory


class Bot:
    def __init__(self):
        self.bot_cars = []

    def create_bots(self, amount, arg):
        raise NotImplementedError()


class BotsForEasyGame(Bot):
    def __init__(self):
        super().__init__()
        self.default_car_creator = default_car_for_beginners.CarForBeginners()
        self.map = map_blueprint.Map
        self.easy_game = abstract_factory.EasyGame()

    # road_type holds abstract factory's place!
    def create_bots(self, amount, length_of_road, road_type, configuration_of_iterator_and_data_structure):
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

        return self.bot_cars    

    def define_map(self, length_of_road, road_type, configuration_of_iterator_and_data_structure):
        defined_map = self.map(length_of_road, road_type)

        defined_map.set_iterator(configuration_of_iterator_and_data_structure)

        return defined_map