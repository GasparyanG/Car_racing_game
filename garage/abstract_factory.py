from garage import data_structure_implementor
from garage.interaction import interaction_with_garage_implementor

class Configuration:
    def give_me_data_structure(self):
        raise NotImplementedError()

    def give_me_interaction(self):
        raise NotImplementedError()


class ConfigurationOfDictinaryTypes:
    def give_me_data_structure(self):
        return data_structure_implementor.DictionaryImplementor()

    def give_me_interaction(self):
        # initialization will be done in garage_for_car.py module
        return interaction_with_garage_implementor.InteractionWithDictionary            