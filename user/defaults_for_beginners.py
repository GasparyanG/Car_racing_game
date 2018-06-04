import default_car_for_beginners
from garage import garage_for_car

class Defaults:
    def give_me_a_car(self):
        raise NotImplementedError()

    def give_me_a_garage(self):
        raise NotImplementedError()

    def give_me_a_points(self):
        raise NotImplementedError()     


class DefaultsForBeginners(Defaults):
    def give_me_a_car(self):
        car = default_car_for_beginners.CarForBeginners().give_me_car()

        return car

    def give_me_a_garage(self):
        # to instanciate garage need user
        return garage_for_car.Garage

    def give_me_a_points(self):
        return 500