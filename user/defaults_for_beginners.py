from implementor_and_decorator_of_car_engine.car_properties import base_case_for_car_engine
from implementor_and_decorator_of_car_engine import car_blueprint
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
        base_engine_for_beginner = base_case_for_car_engine.BaseCaseForBeginner()
        car = car_blueprint.Car()
        car.set_car_base_engine(base_engine_for_beginner)

        return car

    def give_me_a_garage(self):
        # to instanciate garage need user
        return garage_for_car.Garage

    def give_me_a_points(self):
        return 500