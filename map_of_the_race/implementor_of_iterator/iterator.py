class Iterator:
    def __init__(self):
        # self.previous = None
        # self.next = None
        self.current = 0
        self.data_structure = None

    def set_data_structure(self, new_data_structure):
        self.data_structure = new_data_structure

    def next_item(self):
        raise NotImplementedError()        

    def previous_item(self):
        raise NotImplementedError()        

    def current_item(self):
        raise NotImplementedError()        


class DictionaryIterator(Iterator):
    def __init__(self):
        super().__init__()
        self.from_dictionary_to_list = None  

    def next_item(self):
        self.convert_dictionary_to_list()

        self.has_next()
        return self.from_dictionary_to_list[self.current] 

    def has_next(self):
        last_index_of_data_structure = len(self.from_dictionary_to_list) - 1

        if self.current + 1 <= last_index_of_data_structure:
            self.current = self.current + 1

    def previous_item(self):
        self.convert_dictionary_to_list()

        self.has_previous()
        return self.from_dictionary_to_list[self.current]

    def has_previous(self):
        first_index = 0
        
        if self.current -1 >= first_index:
            self.current = self.current - 1

    def current_item(self):
        self.convert_dictionary_to_list()

        return self.from_dictionary_to_list[self.current]        

    def convert_dictionary_to_list(self):
        list_data_structure = []

        for key in sorted(self.data_structure.keys()):
            list_data_structure.append(self.data_structure[key])

        self.from_dictionary_to_list = list_data_structure

    def give_me_current_road_side(self):
        for index, key in enumerate(sorted(self.data_structure.keys())):
            if index == self.current:
                return key    