from random import choice

# This class will be initialized by car (car_blueprint.py) object,
# which will inject its current implementor of engine by constructor of decorater 

# Decorater absract class with its concrete decoraters
class EngineDecorator:
    def __init__(self):
        self.product_to_decorate = None
        self.update_power = None  
        self.price = None
 
    def set_product_to_decorate(self, product):
        self.product_to_decorate = product

    # Templete method, which will be changed by every derived class
    # if there is any change made
    def speed_generator(self):
        self.set_update_power()
        return self.random_generator_of_power()
 
    def random_generator_of_power(self):
        random_speed = choice([speed for speed in range(self.update_power)])
        return random_speed                   

    def turn_left(self):
        raise NotImplementedError()

    def drive_directly(self):
        raise NotImplementedError()

    def turn_right(self):
        raise NotImplementedError()

    def set_update_power(self):
        raise NotImplementedError()
        
    def total_speed(self):
        try:
            return self.product_to_decorate.total_speed() + self.update_power
        except AttributeError:
            return False

    def __str__(self):
        representation = "Average increase of this engine is {}\n".format(self.update_power)
        if self.total_speed():
            representation += "Total speed is {}\n".format(self.total_speed())
        
        representation += "Price: {}\n".format(self.price)    

        return representation   

class EnginePower(EngineDecorator):
    def __init__(self):
        super().__init__()
        self.price = 150
        self.set_update_power() 

    def turn_left(self):
        return self.product_to_decorate.turn_left() + self.speed_generator()

    def drive_directly(self):
        return self.product_to_decorate.drive_directly() + self.speed_generator()

    def turn_right(self):
        return self.product_to_decorate.turn_right() + self.speed_generator()

    def set_update_power(self):
        self.update_power = 15  
        

class EngineSmoothness(EngineDecorator):
    def __init__(self):
        super().__init__()
        self.price = 100
        self.set_update_power()
    
    def turn_left(self):
        return self.product_to_decorate.turn_left() + self.speed_generator()

    def drive_directly(self):
        return self.product_to_decorate.drive_directly()

    def turn_right(self):
        return self.product_to_decorate.turn_right() + self.speed_generator()

    def set_update_power(self):
        self.update_power = 5          