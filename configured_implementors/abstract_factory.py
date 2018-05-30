import car_notifier, map_updater 

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
        return car_notifier.NotifierInHardRoad

    def update_the_state(self, map):
        return map_updater.UpdaterInHardRoad


class EasyGame(AbstractFactory):
    def is_used(self, comparabel_obect):
        return comparabel_obect == "2" 

    def notify_about_changes(self):
        return car_notifier.NotifierInEasyRoad

    def update_the_state(self, map):
        return map_updater.UpdaterInEasyRoad    