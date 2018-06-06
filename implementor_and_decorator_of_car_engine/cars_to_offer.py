from implementor_and_decorator_of_car_engine.car_properties import base_case_for_car_engine
from implementor_and_decorator_of_car_engine import car_blueprint


class CarOffer:
    def __init__(self):
        self.base_class = base_case_for_car_engine.BaseCaseEngineOfCar
        self.car_type = car_blueprint.Car

    def cars_base_cases(self):
        base_cases = self.base_class.__subclasses__()

        return base_cases

    def return_default_cars(self):
        list_of_cars = []

        for base_case in self.cars_base_cases():
            car = self.car_type()
            car.set_car_base_engine(base_case())
            list_of_cars.append(car)

        return list_of_cars    