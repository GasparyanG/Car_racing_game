class DataStructureImplementor:
    def __init__(self):
        self.user = None

    def set_user(self, new_user):
        self.user = new_user

    # def have_engine(self, engine):
    #     raise NotImplementedError()

    # def have_wheel(self, wheel):
    #     raise NotImplementedError()

    def add_engine(self, engine):
        raise NotImplementedError()

    def add_wheel(self, wheel):
        raise NotImplementedError()            
        
    # def have_car(self, car):
    #     raise NotImplementedError() 

    def add_car(self, car):
        raise NotImplementedError()


# {car: [[engine], [wheel]], same key value pair}
class DictionaryImplementor(DataStructureImplementor):
    def __init__(self):
        super().__init__()
        self.data_structure = {}

    # def add_car(self, car):
    #     # first nested list will store engines of car
    #     # second will store wheels of car
    #     self.data_structure[car] = [[],[]]

    def add_car(self, car):
        for key in self.data_strucutre:
            if key.car_model == car.car_model:
                print("{} you already have this car in your garage!".format(self.user.username))
                return True
            # else:
            #     cycle will end 
            #     and None will be returned                     

        self.data_structure[car] = [[],[]]    

    def add_wheel(self, wheel):
        # wheel still need to be defined
        pass   

    def add_engine(self, engine):
        properties_of_car = self.give_me_properties_of_car()
        
        # engine is in first nested list
        list_of_engine_objects = properties_of_car[0]

        for engine_object in list_of_engine_objects:
            if type(engine_object) == type(engine):
                print("{} you car already have this engine".format(self.user.username))
                return True

        list_of_engine_objects.append(engine)        
         
    def give_me_properties_of_car(self):
        current_car = self.user.car
        properties_of_car = self.data_structure[current_car]

        return properties_of_car