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