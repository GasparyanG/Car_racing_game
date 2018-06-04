from implementor_and_decorator_of_car_engine.car_properties import base_case_for_car_engine
from implementor_and_decorator_of_car_engine import car_blueprint

class Defaults:
    def give_me_car(self):
        raise NotImplementedError()


class CarForBeginners(Defaults):
    def give_me_car(self):
        base_engine_for_beginner = base_case_for_car_engine.BaseCaseForBeginner()
        car = car_blueprint.Car()
        car.set_car_base_engine(base_engine_for_beginner)

        return car