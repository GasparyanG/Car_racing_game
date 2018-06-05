from market_implementors import option_to_offer, factory_method
from race import race_complexity_implementor


class Race:
    def __init__(self, user):
        self.user = user
        self.offering_options = option_to_offer.OptionsToChoose()
        self.base_class = race_complexity_implementor.GameComplexity
        self.factory = factory_method.Factory() 

    def is_used(self, comparable_object):
        return comparable_object == "1"

    def execute(self):
        while True:
            # integer will be returnd
            user_choice = self.offering_options.offer(self.base_class)
            desired_race = self.factory.create(user_choice, self.base_class, self.user)

            result_of_race = desired_race.execute()

            # there also will be leave option!  
            if result_of_race:
                break