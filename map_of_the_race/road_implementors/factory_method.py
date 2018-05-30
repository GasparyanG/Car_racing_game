class Factory:
    def create(self, comparable_object, base_class):
        products = self.give_me_subclasses_of_base_class(base_class)

        for product in products:
            product = product()
            if product.is_used(comparable_object):
                return product

    def give_me_subclasses_of_base_class(self, base_class):
        subclasses = base_class.__subclasses__()

        return subclasses    
