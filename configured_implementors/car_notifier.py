class Notifier:
    def __init__(self, car):
        self.car = car

    def notify(self, speed, side):
        raise NotImplementedError()

class NotifierInHardRoad(Notifier):
    def notify(self, speed, side):
        return self.car.map.update_the_state(speed, side, self.car.wheel.type)

class NotifierInEasyRoad(Notifier):
    def notify(self, speed, side):
        return self.car.map.update_the_state(speed, side, None)    