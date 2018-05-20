class Updater:
    def __init__(self, map):
        self.map = map
        self.type_of_complexity = None

    def update(self, speed, wheel_type = None):
        raise NotImplementedError()

    def set_complexity_type(self):
        raise NotImplementedError()    


class UpdaterInHardRoad(Updater):
    def update(self, speed, wheel_type):
        if self.map.type == wheel_type:
            self.map.length = self.map.length - speed

        else:
            # this means that car's wheels don't match to the road 
            speed = speed - 5
            self.map.lenght = self.map.length - speed

    def set_complexity_type(self):
        self.type_of_complexity = "hard"


class UpdaterInEasyRoad(Updater):
    def update(self, speed, wheel_type):
        self.map.lenght = self.map.length - speed

    def set_complexity_type(self):
        self.type_of_complexity = "easy"