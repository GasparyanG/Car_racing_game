from user import user_of_game, defaults_for_beginners
from market_implementors import market_to_buy_stuff
from race import start_of_race

class ImplementorOfStart:
    def __init__(self):
        self.user = user_of_game.User
        self.defaults = defaults_for_beginners.DefaultsForBeginners()
        self.race = start_of_race.Race
        self.market = market_to_buy_stuff

    def start_game(self):
        raise NotImplementedError()

    def is_valid(self, user_choice, list_data_structure):
        list_of_numbers = []

        for number in range(len(list_data_structure)):
            list_data_structure.append(number + 1)

        try:
            user_choice = int(user_choice)
            if user_choice in list_of_numbers:
                return user_choice

        except ValueError:
            return False        


class RegularStart(ImplementorOfStart):
    def start_game(self):
        self.user_creation() 
        
        info = self.representation_of_options()
        representation_of_options = info[0]
        list_of_options = info[1]

        while True:
            print(representation_of_options)
            user_choice = input("Choose option by typing corresponding number: ")
            
            if user_choice == "L" or user_choice == "l":
                print("Goodby {}".format(self.user.username))
                break

            user_choice = self.is_valid(user_choice, list_of_options)    
            if not user_choice:
                print("Don't violate the requirements!")
                continue

            desired_option = list_of_options[user_choice]

            desired_option.execute() 

    def user_creation(self):
        print("Hello there!")
        username = input("Write your username: ")

        self.user = self.user(username)

        self.user.set_standards_for_beginners(self.defaults)

    def create_list_of_options(self):
        list_of_options = []

        self.race = self.race(self.user)
        list_of_options.append(self.race)

        self.market = self.market(self.user)
        list_of_options.append(self.market)

        garage_of_user = self.user.give_me_current_garage()
        list_of_options.append(garage_of_user)

        return list_of_options

    def representation_of_options(self):
        list_of_options = self.create_list_of_options()

        representation = "If you want to leave type L\n"
        for index, option in enumerate(list_of_options):
            representation += "{}){}\n".format(index + 1, option.name)

        return [representation, list_of_options]        