from race import configuration, commands_to_car
from market_implementors import factory_method


class GameComplexity:
    def __init__(self, user):
        self.user = user
        self.game_complexity = None

    def is_used(self, comparable_object):
        raise NotImplementedError()    
    
    def execute(self):
        raise NotImplementedError()

    def create_map_for_user(self):
        raise NotImplementedError()
        

class EasyGame(GameComplexity):
    def __init__(self, user):
        super().__init__(user)
        self.commands = commands_to_car.CommandsToCar
        self.configuration_of_map_and_car = configuration.EasyGameConfiguration()
        self.factory = factory_method.Factory()

    def is_used(self, comparable_object):
        return comparable_object == 1

    def execute(self):
        while True:
            print("You can have up to 10 oponents!\nBy default you will have 5 oponents!")
            user_decision = input("Type number of oponents you want: ")
            
            amount_of_oponents = self.is_valid(user_decision)
            # this method will set user's map also (Violation of SRP)
            list_of_arguments = self.create_map_for_user()
            object_creating_oponents = self.configuration_of_map_and_car.give_me_default_bots()

            bots = object_creating_oponents.create_bots(amount_of_oponents, list_of_arguments)

            result_of_race = self.process_of_race(bots)     
            if result_of_race:
                break

    def process_of_race(self, bots):
        representation = self.representation_of_commands()
        
        while True:
            print(self.what_is_going_on())              

            # user have to know what is going on:
            # distance left to finish (also for oponents)
            # amount of oponents

            print(representation)

            user_choice = input("To make move type corresponding option: ")

            users_car = self.user.give_me_current_car()
            # factory will call commands on car object, which in its turn will call
            # maps corresponding method 
            command_object = self.factory.create(user_choice, self.commands, users_car)
            
            if not command_object:
                print("Don't violate the requirements!")
                continue
            
            result_from_factory = command_object.to_command()
            if not result_from_factory:
                print("Don't violate the requirements!")
                continue

            elif type(result_from_factory) == int:
                self.user.points += result_from_factory

            else:
                users_car.update_engine(result_from_factory)

            state_of_users_map = self.end_of_race(users_car)

            if state_of_users_map:
                return True    

            for bot in bots:
                # print distance of road, which is left until finish.
                bot.random_own_method_calling()
                
                state_of_race = self.end_of_race(bot)
                if state_of_race:
                    return True


    def end_of_race(self, car):
        if car.is_finished():
            print("{} is winner!".format(car.name))
            return True 

    def representation_of_commands(self):
        commands = self.commands.__subclasses__()

        representation = ""
        for command in commands:
            command = command(self.user.give_me_current_car())
            representation += "{}\n".format(command.__str__())

        return representation     

    def create_map_for_user(self):
        users_map = self.configuration_of_map_and_car.give_me_implementor_of_creator()

        # this sets not only user's car's map but also returns arguments for bot's map
        list_of_arguments = users_map.define_users_cars_map(self.user)

        return list_of_arguments

    def is_valid(self, user_decision):
        list_of_numbers = []
        
        for number in range(10):
            list_of_numbers.append(number + 1) 

        try:
            user_decision = int(user_decision)
            if user_decision in list_of_numbers:
                return user_decision

            else:
                # exception mey not raise
                return 4    

        except ValueError:
            # by default there will be 5 oponents!
            return 4         

    def what_is_going_on(self):
        car = self.user.give_me_current_car()
        current_map = car.give_me_current_map()

        representation = "Distance left: {}\n".format(current_map.length)
        representation += "Side of the road, where you are at this moment: {}\n".format(current_map.give_me_side_of_road()) 

        return representation


class LeaveRace(GameComplexity):
    def is_used(self, comparable_object):
        return comparable_object == 2

    def execute(self):
        return True    