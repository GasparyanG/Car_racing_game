# which method in its definitiona name have "have"
# boolen will be returned:
#     true if have
#     false if don't have 

class Garage:
    def __init__(self):
        self.user = None
        self.data_structure_impelementor = None

    def is_used(self, comparable_object):
        return comparable_object == "3" 

    def set_user(self, new_user):
        self.uesr = new_user    

    def set_data_structure_impelementor(self, new_implementor):
        self.data_structure_impelementor = new_implementor

    # def have_engine(self, engine):
    #     pass

    # def have_wheel(self, wheel):
    #     pass

    def add_engine(self, engine):
        pass

    def add_wheel(self, wheel):
        pass            
        
    # def have_car(self, car):
    #     pass 

    def add_car(self, car):
        pass        