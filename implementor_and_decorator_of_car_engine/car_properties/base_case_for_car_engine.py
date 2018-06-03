# Mostly recursion need to have base case
# and because of the fact that decorator pattern
# is based on recursion here is it's base case!  

class BaseCaseEngineOfCar:
    def __init__(self):
        self.maximum_speed_of_car = None
        self.model = None
        self.price = None

    def turn_left(self):
        raise NotImplementedError()

    def drive_directly(self):
        raise NotImplementedError()

    def turn_right(self):
        raise NotImplementedError()

    def total_speed(self):
        total = self.turn_left() + self.turn_right() + self.drive_directly()
        average = total // 3 

        return average

    def __str__(self):
        representation = "Average speed of this engine is {}\n".format(self.total_speed())
        representation += "Price: {}\n".format(self.price)

        return representation   


class FastCarBaseCase(BaseCaseEngineOfCar):
    def __init__(self):
        self.maximum_speed_of_car = 250
        self.model = "Ferrari"
        self.price = 2000

    def turn_left(self):
        return 50

    def drive_directly(self):
        return 75

    def turn_right(self):
        return 50


class BaseCaseForBeginner(BaseCaseEngineOfCar):
    def __init__(self):
        self.maximum_speed_of_car = 150
        self.model = "Opel"
        self.price = 0

    def turn_left(self):
        return 25

    def drive_directly(self):
        return 50

    def turn_right(self):
        return 25


class MediumCarBaseCase(BaseCaseEngineOfCar):
    def __init__(self):
        self.maximum_speed_of_car = 200
        self.model = "Audi"
        self.price = 1500
    
    def turn_left(self):
        return 35

    def drive_directly(self):
        return 60

    def turn_right(self):
        return 35