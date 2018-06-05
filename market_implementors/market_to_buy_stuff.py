from market_implementors import buy_stuff_implementors

class Market:
    def __init__(self, user):
        self.name = "Market"
        # user will hold a car
        # car will hold a map
        self.user = user 
        self.buy_implementor = buy_stuff_implementors.BuyingStuff(self.user)

    def is_used(self, comparable_object):
        # human familiar indexing
        # first offer will be a race
        return comparable_object == "2"

    # buy_stuff  
    def execute(self):
        self.buy_implementor.buy()

    def set_buy_implementor(self, new_implementor):
        self.buy_implementor = new_implementor(self.user)    