from random import choice

class Obsteacle:
    def __init__(self):
        self.product_to_decorate = None
        self.reduceing_range = None  

    def speed_generator(self):
        self.set_reduceing_range()
        return self.random_generator_of_power()
 
    def random_generator_of_power(self):
        random_speed = choice([speed for speed in range(self.reduceing_range)])
        return random_speed                   

    def turn_left(self):
        raise NotImplementedError()

    def drive_directly(self):
        raise NotImplementedError()

    def turn_right(self):
        raise NotImplementedError()

    def set_reduceing_range(self):
        raise NotImplementedError()

    def set_product_to_decorate(self, new_product):
        self.product_to_decorate = new_product    

    def __str__(self):
        representation = "Obsteacle's type is {}\n".format(type(self).__name__)
        representation += "reducing range is {}\n".format(self.reduceing_range)

        return representation
        

class WinterObsteacle(Obsteacle):
    def turn_left(self):
        return self.product_to_decorate.turn_left() - self.speed_generator()

    def drive_directly(self):
        return self.product_to_decorate.drive_directly() - self.speed_generator()

    def turn_right(self):
        return self.product_to_decorate.turn_right() - self.speed_generator()

    def set_reduceing_range(self):
        self.update_power = 20


class AutumnObsteacle(Obsteacle):
    def turn_left(self):
        return self.product_to_decorate.turn_left() - self.speed_generator()

    def drive_directly(self):
        return self.product_to_decorate.drive_directly() - self.speed_generator()

    def turn_right(self):
        return self.product_to_decorate.turn_right() - self.speed_generator()

    def set_reduceing_range(self):
        self.update_power = 10