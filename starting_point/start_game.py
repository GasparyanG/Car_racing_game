from starting_point import implementor_of_start

class UnionOfGameParts:
    def __init__(self):
        self.start_implementor = implementor_of_start.RegularStart()
        
    def set_start_implementor(self, new_implementor):
        self.start_implementor = new_implementor

    def start(self):
        self.start_implementor.start_game()     


game = UnionOfGameParts()
game.start()           