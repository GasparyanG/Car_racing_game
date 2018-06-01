class Notifier:
    def __init__(self, car):
        self.car = car

    def notify(self, speed):
        raise NotImplementedError()

class NotifierInHardRoad(Notifier):
    def notify(self, speed):
        self.car.map.update_the_state(speed, self.car.wheel.type)

class NotifierInEasyRoad(Notifier):
    def notify(self, speed):
        self.car.map.update_the_state(speed, None)    