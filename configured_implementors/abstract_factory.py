from car_notifier import NotifierInHardRoad, NotifierInEasyRoad
from map_updater import UpdaterInHardRoad, UpdaterInEasyRoad

class AbstractFactory:
    def is_used(self, comparabel_obect):
        raise NotImplementedError() 

    def notify_abouti_changes(self):
        raise NotImplementedError()

    def update_the_state(self):
        raise NotImplementedError()


class HardGame(AbstractFactory):
    def is_used(self, comparabel_obect):
        return comparabel_obect == "1" 

    def notify_about_changes(self):
        return NotifierInHardRoad

    def update_the_state(self):
        return UpdaterInHardRoad


class EasyGame(AbstractFactory):
    def is_used(self, comparabel_obect):
        return comparabel_obect == "2" 

    def notify_about_changes(self):
        return NotifierInEasyRoad

    def update_the_state(self):
        return UpdaterInEasyRoad    