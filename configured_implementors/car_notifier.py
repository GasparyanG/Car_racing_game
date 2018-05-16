class Notifier:
    def __init__(self, car):
        self.car = car

    def notify(self, speed):
        raise NotImplementedError()


class NotifierInHardRoad(Notifier):
    def notify(self, speed):
        self.car.map.update(speed, self.car.wheel)


class NotifierInEasyRoad(Notifier):
    def __init__(self, car):
        self.car = car

    def notify(self, speed):
        self.car.map.update(speed)    
