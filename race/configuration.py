from oponents import programme_made_cars
from race.users_map_creation import implementor_of_creation


class Configuration:
    def give_me_default_bots(self):
        raise NotImplementedError()

    def give_me_implementor_of_creator(self):
        raise NotImplementedError()


class EasyGameConfiguration(Configuration):
    def __init__(self):
        self.bots = programme_made_cars.BotsForEasyGame()
        self.creator_of_map = implementor_of_creation.MapCreatorForEasyGame() 

    def give_me_default_bots(self):
        return self.bots

    def give_me_implementor_of_creator(self):
        return self.creator_of_map            