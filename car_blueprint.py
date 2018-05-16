# from configured_implementations import abstract_factory

class Car:
    def __init__(self, speed, model):
        self.notifier = None
        self.map = None 
        self.speed = speed
        self.model = model
    
    def turn_left(self):
        pass      
    
    def notify(self, speed):
        self.notifier.notify(speed)

    def set_map(self, new_map):
        self.map = new_map

    def set_notifier(self, new_abstract_factory):
        notifier = new_abstract_factory.notify_about_changes()
        self.notifier = notifier(self)

    
                