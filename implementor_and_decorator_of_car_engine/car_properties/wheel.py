import storage_of_road_types

"""
    wheel class have to be initialized to offer,
    for more informatin checkout ../garage/data_structure_implementor!
"""

class Wheel:
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def __srt__(self):
        representation = "Type of wheel: {}\n".format(self.type)
        representation += "Price of wheel: {}\n".format(self.price)

        return representation


def return_instances_of_wheel():
    road_types = storage_of_road_types.dictionary_of_road_types

    list_of_wheels = []
    for road_type in road_types:
        wheel_object = Wheel(road_type, road_types[road_type])
        list_of_wheels.append(wheel_object)

    return list_of_wheels     