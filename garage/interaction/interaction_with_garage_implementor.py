from garage import factory_method
from garage.interaction import deep_implementor_of_execute

class UsersInteraction:
    def __init__(self, data_structure_implementor, garage, user):
        self.data_structure_implementor = data_structure_implementor
        self.garage = garage
        self.user = user

    def is_used(self, comparable_object):
        raise NotImplementedError()

    def execute(self):
        raise NotImplementedError()


class InteractionWithDictionary(UsersInteraction):
    def __init__(self, data_structure_implementor, garage, user):
        super().__init__(data_structure_implementor, garage, user)
        self.factory = factory_method.Factory(self.data_structure_implementor, self.garage, self.user)
        self.base_class = deep_implementor_of_execute.DeepImplementor

    def is_used(self, comparable_object):
        return comparable_object == "3"

    def execute(self):
        info = self.representing_functions_of_garage()
        prompt = info[0]
        amount_of_operations = info[1]

        while True:
            print(prompt)
            user_choice = input("Choose option by typing corresponding number: ")

            if not self.is_valid(user_choice, amount_of_operations):
                print("Don't violate the requirements! ")            
                continue
            
            desired_implementor = self.factory.create(user_choice, self.base_class)
            
            executing_choosen_operation = desired_implementor.execute()
            
            if executing_choosen_operation:
                break
             
    def is_valid(self, user_choice, amount_of_operations):
        list_of_numbers = []

        for number in range(amount_of_operations):
            list_of_numbers.append(number + 1)

        try:
            if int(user_choice) in list_of_numbers:
                return True
        except ValueError:
            return False    

    def representing_functions_of_garage(self):
        data_stucture_representation = self.data_structure_implementor.data_structure_representation
        # obviously this is a dictionary:
        # name of this class reveals all
        
        # key of this dictionary is of car type
        # value is list which in its turn have two sublists
        # first stores engines of car which will not be used by garage
        # second stores wheels of car which will be used
        
        # dictionary will store only one key : value pair

        prompt_for_user = "Change if you want to or leave\n" 
        amount_of_operations = 0
        
        for index, key in enumerate(data_stucture_representation):
            prompt_for_user += "{}){}\n".format(index + 1, key)
            amount_of_operations += 1

        value_of_given_key = data_stucture_representation[key] 

        for index, item in enumerate(value_of_given_key):
            # first item is engine, which, as above already mentioned, won't be used! 
            if index == 0:
                continue

            # item takes index because it is a nested list:
            # this list will have only one item in it becaouse it is only a representation  
            prompt_for_user += "{}){}\n".format(index + 1, item[0])
            amount_of_operations += 1

        prompt_for_user += "{})Leave".format(index + 2)
        amount_of_operations += 1

        return [prompt_for_user, amount_of_operations]      