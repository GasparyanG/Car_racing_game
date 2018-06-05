class CommandsToCar:
    def __init__(self, car):
        self.car = car

    def is_used(self, comparable_object):
        raise NotImplementedError()

    def to_command(self):
        raise NotImplementedError()    

    def return_turn_operand(self):
        raise NotImplementedError()
    
    def __str__(self):
        representation = "{}: {}".format(type(self).__name__, self.return_turn_operand())

        return representation
        

class TurnLeft(CommandsToCar):
    def is_used(self, comparable_object):
        return comparable_object == "A"

    def to_command(self):
        return self.car.turn_left()

    def return_turn_operand(self):
        return "A"   


class DriveDirectly(CommandsToCar):
    def is_used(self, comparable_object):
        return comparable_object == "W"

    def to_command(self):
        return self.car.drive_directly()

    def return_turn_operand(self):
        return "W"   


class TurnRight(CommandsToCar):
    def is_used(self, comparable_object):
        return comparable_object == "D"

    def to_command(self):
        return self.car.turn_right()            

    def return_turn_operand(self):
        return "D"  