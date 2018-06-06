import random

class DataStructureImplementor:
    def __init__(self, data_structure, obsteacle, points):# , game_complexity):
        self.data_structure = data_structure
        self.obsteacle = obsteacle
        self.points = points
        # self.game_complexity = game_complexity

    def is_used(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def random_generation(self):
        list_of_points = [] 
        for point in range(self.points):
            list_of_points.append(point)

        list_of_points.append(self.obsteacle)

        random.shuffle(list_of_points)
        random_one = random.choice(list_of_points)
        return random_one


class DictionaryImplementor(DataStructureImplementor):
    def is_used(self):
        return type(self.data_structure) == dict

    def update(self):
        for key in self.data_structure:
            self.data_structure[key] = self.random_generation()

        return self.data_structure    


class ListImplementor(DataStructureImplementor):
    def is_used(self):
        return type(self.data_structure) == list

    def update(self):
        # list in this scenario can be [None, None, None]
        for index, item in enumerate(self.data_structure):
            self.data_structure[index] = self.random_generation()

        return self.data_structure   