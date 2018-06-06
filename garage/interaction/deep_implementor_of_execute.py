class DeepImplementor:
    def __init__(self, data_structure_implementor, garage, user):
        self.data_structure_implementor = data_structure_implementor
        # to get a car garage can offer give_me_current_car() method
        
        self.garage = garage  
        self.user = user

    def is_valid(self, user_choice, list_data_structure):
        list_of_numbers = []
        for number in range(len(list_data_structure)):
            list_of_numbers.append(number + 1)     

        try:
            user_choice = int(user_choice)
            if user_choice in list_of_numbers:
                return user_choice
        except ValueError:
            return False
    
    def is_used(self, comparable_object):
        raise NotImplementedError()

    def execute(self):
        raise NotImplementedError()

    def leave(self, user_choice):
        if user_choice == "L" or user_choice == "l":
            return True


class CarOffer(DeepImplementor):
    def is_used(self, comparable_object):
        return comparable_object == "1"

    def execute(self):
        info_about_cars = self.representing_cars_in_data_structure()
        cars_representation = info_about_cars[0]
        cars_list = cars_representation[1]

        while True:
            print(cars_representation)
            print("If you want to leave type L!")
            user_choice = input("Choose car by typing correspoinding number: ")

            user_choice = self.is_valid(user_choice, cars_list)

            if self.leave(user_choice):
                break

            if not user_choice:
                print("Don't violate the requirements!")
                continue

            self.change_users_car(user_choice, cars_list)
            
            break

    def change_users_car(self, user_choice, cars_list):
        programming_common_index = user_choice - 1
        car = cars_list[programming_common_index]

        self.user.car = car            
                                
    def representing_cars_in_data_structure(self):
        data_structure = self.data_structure_implementor.data_structure

        cars_representation = ""
        cars_list = []
        for index, car in enumerate(data_structure):
            cars_representation += "{}){}\n".format(index + 1, car.__str__())
            cars_list.append(car)

        return [cars_representation, cars_list]    

                 
class WheelOffer(DeepImplementor):
    def is_used(self, comparable_object):
        return comparable_object == "2"

    def execute(self):
        users_current_car = self.user.give_me_current_car()
        info_about_wheels = self.representing_wheels_of_current_car(users_current_car)

        wheel_representation = info_about_wheels[0]
        wheels_list = info_about_wheels[1]

        while True:
            print(wheel_representation)
            print("If you want to leave type L!")

            user_choice = input("Choose wheel by typing corresponding number: ")

            if self.leave(user_choice):
                break

            user_choice = self.is_valid(user_choice, wheels_list)  
            if not user_choice:
                print("Don't violate the requirements!")
                continue

            self.change_wheel_on_current_car(user_choice, wheels_list, users_current_car)

            break

    def representing_wheels_of_current_car(self, users_current_car):
        data_structure = self.data_structure_implementor.data_structure
        print(users_current_car)

        properties_of_car = data_structure[users_current_car]
        wheels_of_car = properties_of_car[1]

        wheel_representation = ""
        wheels_list = []

        for index, wheel in enumerate(wheels_of_car):
            wheel_representation += "{}){}\n".format(index + 1, wheel.__str__())
            wheels_list.append(wheel)

        return [wheel_representation, wheels_list]    

    def change_wheel_on_current_car(self, user_choice, wheels_list, current_car):
        programming_common_index = user_choice - 1
        desired_wheel = wheels_list[programming_common_index]

        current_car.set_wheel(desired_wheel)    


class LeaveGarage(DeepImplementor):
    def is_used(self, comparable_object):
        return comparable_object == "3"

    def execute(self):
        return True        