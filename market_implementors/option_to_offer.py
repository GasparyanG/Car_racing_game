class OptionsToChoose:
    def offer(self, base_class):
        while True:    
            info = self.options_representation(base_class)
            print(info[0])
            user_choice = input("Choose option by typing corresponding umber: ")
    
            user_choice = self.is_valid(user_choice, info[1]) 
            if user_choice:
                return user_choice
            
            else:
                print("Don't violate the requirements!") 

    def options_representation(self, base_class):
        subclasses = base_class.__subclasses__()

        prompt = ""  
        for index, subclass in enumerate(subclasses):
            prompt += "{}){}\n".format(index + 1, subclass.__name__)

        return [prompt, subclasses]     

    def is_valid(self, user_choice, list_of_subclasses):
        list_of_numbers = []

        for number in range(len(list_of_subclasses)):
            list_of_numbers.append(number + 1)

        try:
            user_choice = int(user_choice)
            if user_choice in list_of_numbers:
                return user_choice
        except ValueError:
            return False        