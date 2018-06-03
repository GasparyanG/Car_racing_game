class Factory:
    def __init__(self, data_structure_implementor, garage, user):
        self.data_structure_implementor = data_structure_implementor
        self.garage = garage
        self.user = user    

    def create(self, comparable_object, base_class):
        products = self.products_to_be_created(base_class)

        for product in products:
            product = product(self.data_structure_implementor, self.garage, self.user)
            if product.is_used(comparable_object):
                return product

    def products_to_be_created(self, base_class):
        products = base_class.__subclasses__()

        return products