class User:
    def __init__(self, username):
        # user will be asked for name
        # other properties of user will be injected
        # by default
        self.username = username 
        self.car = None
        self.garage = None
        self.points = None

    def set_standards_for_beginners(self, new_standards):
        # new standards will be an abstract factory holding multiaple products
        self.car = new_standards.give_me_a_car()
        self.garage = new_standards.give_me_a_garage()
        self.pointss = new_standards.give_me_a_points()

    def set_car(self, new_car):
        self.car = new_car

    def set_garage(self, new_garage):
        self.garage = new_garage(self)

    def add_points(self, points):
        self.points = self.points + points              
        
    def set_engine(self, new_engine):
        # user don't need to be (is a: inheritance) a garage to
        # change engine instead user can have (has a: composition) garage 
        # implementing on its own         
        pass

    def update_car_engine(self, engine):
        self.car.update_engine(engine)    

    def add_new_car(self, new_car):
        pass 

    def add_new_wheel(self, new_wheel):
        # also the same situation:
        # composition over inheritance!
        pass

    def give_me_current_car(self):
       return self.car             