# from configured_implementations import abstract_factory

class Car:
    def __init__(self, speed, model):
        self.notifier = None
        self.map = None 
        self.engine = None
        self.speed = speed
        self.model = model
        # self.problem = 0
    
    def turn_left(self):
        speed = self.engine.turn_left()      
        self.notify(speed)   

    def drive_directly(self):
        speed = self.engine.drive_directly()
        self.notify(speed)

    def turn_right(self):
        speed = self.engine.turn_right()
        self.notify(speed)

    def notify(self, speed):
        self.notifier.notify(speed)

    def set_map(self, new_map):
        self.map = new_map

    def set_notifier(self, new_abstract_factory):
        notifier = new_abstract_factory.notify_about_changes()
        self.notifier = notifier(self)

    def update_engine(self, new_futures):
        """
            if type(new_futures) == obsteacle:
                self.problems += 1
        """        
        self.engine = new_futures(self.engine)     
                


                