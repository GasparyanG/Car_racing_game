from map_of_the_race.implementor_of_iterator import iterator


class Configuration:
    def give_me_iterator(self):
        raise NotImplementedError()

    def give_me_data_structure(self):
        raise NotImplementedError()


class ConfigurationOfDictionary(Configuration):
    def __init__(self):
        self.iterator_of_dictionary = iterator.DictionaryIterator()
    
    def give_me_iterator(self):
        return self.iterator_of_dictionary
    
    def give_me_data_structure(self):
        return {"Left" : None, "Middle" : None, "Right" : None}