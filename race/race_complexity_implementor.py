from configured_implementors import abstract_factory


class GameComplexity:
    def __init__(self, user):
        self.user = user
        self.game_complexity = None

    def is_used(self, comparable_object):
        raise NotImplementedError()    
    
    def execute(self):
        raise NotImplementedError()

    def create_map_for_user(self):
        # this will be defind in another scope!
        pass 
        

class EasyGame(GameComplexity):
    def __init__(self, user):
        super().__init__(user)
        self.game_complexity = abstract_factory.EasyGame()

    def is_used(self, comparable_object):
        return comparable_object == "1"

    def execute(self):
        pass
