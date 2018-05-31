# this can be another base case for decoratora patter

# As this class will be injected into different car objects with SETTER,
# it will be initialized inside car object by receiving self as engine's car propertie 


# Strategy with its algorithms
class ImplementorOfCarEngine:
    def __init__(self, car):
        self.car = car

    def turn_left(self):
        raise NotImplementedError()

    def drive_directly(self):
        raise NotImplementedError()

    def turn_right(self):
        raise NotImplementedError()


class SmoothnessGivingEngine(ImplementorOfCarEngine):
    def turn_left(self):
        return self.car.speed - 1

    def drive_directly(self):
        return self.car.speed

    def turn_right(self):
        return self.car.speed - 1


class RegularEngine(ImplementorOfCarEngine):
    def turn_left(self):
        return self.car.speed - 3

    def drive_directly(self):
        return self.car.speed

    def turn_right(self):
        return self.car.speed - 3


class ClumsyEngine(ImplementorOfCarEngine):
    def turn_left(self):
        return self.car.speed - 7

    def drive_directly(self):
        return self.car.speed

    def turn_right(self):
        return self.car.speed - 7