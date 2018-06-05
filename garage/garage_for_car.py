from garage import abstract_factory

# its important to add car into data structure as soon as game starts:
# otherwise called methods will raise exceptions!

class Garage:
    def __init__(self, user):
        self.name = "Garage"
        self.user = user
        self.configuratoin = abstract_factory.ConfigurationOfDictinaryTypes() 
        self.data_structure_impelementor = None
        self.user_friendly_execution = None
        
        self.set_abstract_factory(self.configuratoin)

    """
        is_used method can't be used as before:  
        garage and market are in separate namespaces.
        
        Instead garage, market, race options will be stored in 
        list, whic will be traversed:
            
            for item in list: 
                if item.is_used(comparable_object) returns true:
                    item.do_sth()
    """  
    
    def is_used(self, comparable_object):
        return self.user_friendly_execution.is_used(comparable_object) 
    
    def execute(self):
        self.user_friendly_execution.execute()

    def set_user(self, new_user):
        self.uesr = new_user    

    def set_abstract_factory(self, new_abstract_factory):
        # object will be returned
        self.data_structure_impelementor = new_abstract_factory.give_me_data_structue()
        # this is still of its type
        user_friendly_execution = new_abstract_factory.give_me_interaction()
        self.user_friendly_execution = user_friendly_execution(self.data_structure_impelementor, self, self.user)    

    # This won't be an object
    def set_user_friendly_execution(self, new_execution):
        self.user_friendly_execution = new_execution(self.data_structure_impelementor, self, self.user)

    def set_data_structure_impelementor(self, new_implementor):
        self.data_structure_impelementor = new_implementor

    def add_engine(self, engine):
        return self.data_structure_impelementor.add_engine(engine)

    def add_wheel(self, wheel):
        return self.data_structure_impelementor.add_wheel(wheel)     
        
    def add_car(self, car):
        return self.data_structure_impelementor.add_car(car)