from implementor_and_decorator_of_car_engine.car_properties import decorator_of_car_engine

class CategoriesOfStuff:
    def __init__(self, user):
        self.user = user

    def is_used(self, comparable_object):
        raise NotImplementedError()

    def buy(self):
        raise NotImplementedError()


class Engine(CategoriesOfStuff):
    def __init__(self, user):
        super().__init__(user)
        self.car_engines_base_class = decorator_of_car_engine.EngineDecorator
    
    def set_car_engine_base_class(self, new_base_class):
        self.car_engines_base_class = new_base_class

    def is_used(self, comparable_object):
        return comparable_object == 1

    def buy(self):
        while True:
            info  = self.engines_representation()

            print(info[0])  
            user_choice = input("Choose engine by typing correspoinding number: ")

            user_choice = self.is_valid(user_choice, info[1])
            if not user_choice:
                print("Don't violate the requirements!")
                continue

            choosen_object = info[1][user_choice]
            
            """ 
                To buy "choosen_object" user need to have sufficient amount of money:
                    [] - Define user!
                
                Every object need to have price:
                    [] - object's price

            """

    def is_valid(self, user_choice, list_of_engines):
        list_of_numbers = []

        for number in range(len(list_of_engines)):
            list_of_numbers.append(number + 1)

        try:
            user_choice = int(user_choice)
            if user_choice in list_of_numbers:
                return user_choice
        except ValueError:
            return False        

    def engines_representation(self):
        list_of_engines_blueprint = self.car_engines_base_class.__subclasses__()

        representation = ""
        for index, engine in enumerate(list_of_engines_blueprint):
            description_of_engine = engine().__str__()

            representation += "{}){}\n".format(index + 1, description_of_engine)

        return [representation, list_of_engines_blueprint]