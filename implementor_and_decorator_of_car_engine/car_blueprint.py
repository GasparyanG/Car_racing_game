# If car's engine is fully updated don't let someone to waste money!

# from configured_implementations import abstract_factory
# speed of a car have to be calculated

class Car:
    def __init__(self):
        self.car_wheel = None 
        self.notifier = None
        self.map = None
        self.car_maximum_speed = None
        self.car_model = None
        self.price = None 
        self.engine = None
        self.problems = 0
    
    def turn_left(self):
        side = "L"
        speed = self.engine.turn_left()      
        self.notify(speed, side)   

    def drive_directly(self):
        side = "D"
        speed = self.engine.drive_directly()
        self.notify(speed, side)

    def turn_right(self):
        side = "R"
        speed = self.engine.turn_right()
        self.notify(speed, side)

    def notify(self, speed, side):
        self.notifier.notify(speed, side)

    def set_map(self, new_map):
        self.map = new_map

    def set_notifier(self, new_abstract_factory):
        notifier = new_abstract_factory.notify_about_changes()
        self.notifier = notifier(self)

    def set_car_base_engine(self, base_engine):
        self.engine = base_engine
        self.price = self.engine.price
        self.car_maximum_speed = self.engine.maximum_speed_of_car
        self.car_model = self.engine.model  

    def set_wheel(self, new_wheel):
        self.wheel = new_wheel
    
    def update_engine(self, new_futures):
        if self.map.is_obsteacle(new_futures):
            self.problems += 1
            new_futures.set_product_to_decorate(self.engine)
            self.engine = new_futures

        else:
            if self.engine.drive_directly() + 4 < self.car_maximum_speed:
                new_futures.set_product_to_decorate(self.engine)
                self.engine = new_futures

            else:
                print("Your car is up to date!")

    def __str__(self):
        representation = "Model: {}\n".format(self.car_model)
        representation += "Average speed: {}\n".format(self.engine.turn_left())
        representation += "Maximum speed that this car can have: {}\n".format(self.car_maximum_speed)
                    
        return representation