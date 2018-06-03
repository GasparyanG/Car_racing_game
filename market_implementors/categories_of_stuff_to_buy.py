from implementor_and_decorator_of_car_engine.car_properties import decorator_of_car_engine, wheel
from implementor_and_decorator_of_car_engine import cars_to_offer

class CategoriesOfStuff:
    def __init__(self, user):
        self.user = user

    def is_used(self, comparable_object):
        raise NotImplementedError()

    def buy(self):
        raise NotImplementedError()

    def is_valid(self, user_choice, list_data_structure):
        list_of_numbers = []

        for number in range(len(list_data_structure)):
            list_of_numbers.append(number + 1)

        try:
            user_choice = int(user_choice)
            if user_choice in list_of_numbers:
                return user_choice
       
        except ValueError:
            return False

    def leave(self, user_decision):
        if user_decision == "l" or user_decision == "L":
            return True


class Engine(CategoriesOfStuff):
    def __init__(self, user):
        super().__init__(user)
        self.car_engines_base_class = decorator_of_car_engine.EngineDecorator
    
    def set_car_engine_base_class(self, new_base_class):
        self.car_engines_base_class = new_base_class

    def is_used(self, comparable_object):
        return comparable_object == 1

    def buy(self):
        while True:
            info  = self.engines_representation()

            print(info[0])  
            user_choice = input("Choose engine by typing correspoinding number: ")

            if self.leave(user_choice):
                break 

            user_choice = self.is_valid(user_choice, info[1])
            if not user_choice:
                print("Don't violate the requirements!")
                continue

            choosen_object = info[1][user_choice - 1]

            if self.user.points >= choosen_object.price:
                is_bought = self.user.add_engine(choosen_object) 
                if is_bought:
                    print("You already bought this engine for this car!")

                else:
                    self.user.points = self.user.points - choosen_object.price

            else:
                print("You don't have enough points to buy this engine!")            

    def engines_representation(self):
        list_of_engines_blueprint = self.car_engines_base_class.__subclasses__()

        representation = "If you want to leave type L\n"
        for index, engine in enumerate(list_of_engines_blueprint):
            description_of_engine = engine().__str__()

            representation += "{}){}\n".format(index + 1, description_of_engine)

        return [representation, list_of_engines_blueprint]


class Wheel(CategoriesOfStuff):
    def __init__(self, user):
        super().__init__(user)
        self.wheel_objects = wheel.return_instances_of_wheel()

    def is_used(self, comparable_object):
        return comparable_object == 2

    def buy(self):
        info = self.representataion_of_wheels()

        while True:
            print(info)
            user_choice = input("Choose wheel of car by typing corresponding number: ")
            
            user_choice = self.is_valid(user_choice, self.wheel_objects)

            if self.leave(user_choice):
                # None will be returned
                break

            if not user_choice:
                print("Don't violate the requirements!")
                continue

            desired_wheel = self.wheel_objects[user_choice - 1]    

            if self.user.points >= desired_wheel.price:
                if self.user.add_new_wheel():
                    print("You already bought this wheel for this car!")

                else:
                    self.user.points = self.user.points - desired_wheel.price

            else:
                print("You don't have enough points to buy this wheel!")            


    def representataion_of_wheels(self):
        representation = "If you want to leave type L\n"

        for index, wheel in enumerate(self.wheel_objects):  
            representation += "{}){}\n".format(index + 1, wheel.__srt__())

        return representation


class Car(CategoriesOfStuff):
    def __init__(self, user):
        super().__init__(user)
        self.cars = cars_to_offer.CarOffer()

    def is_used(self, comparable_object):
        return comparable_object == 3

    def buy(self):
        info = self.representation_of_cars()
        representation = info[0]
        list_of_cars = info[1]

        while True:
            print(representation)
            user_choice = input("Choose car by typing corresponding number: ")

            if self.leave(user_choice):
                break

            user_choice = self.is_valid(user_choice, list_of_cars) 
            if not user_choice:
                continue

            desired_car = list_of_cars[user_choice - 1]

            if self.user.points >= desired_car.price:
                is_bought = self.user.add_new_car(desired_car)
                if is_bought:
                    print("You already have this car!")

                else:
                    self.user.points = self.user.points - desired_car.price

            else:
                print("You don't have enough points to buy this car!")                


    def representation_of_cars(self):
        list_of_cars = self.cars.return_default_cars()

        representation = "If you want to leave type L\n"
        for index, car in enumerate(list_of_cars):
            representation += "{}){}\n".format(index + 1, car.__str__())

        return [representation, list_of_cars]                      


class Leave(CategoriesOfStuff):
    def  is_used(self, comparable_object):
        return comparable_object == 4

    def buy(self):
        return True        