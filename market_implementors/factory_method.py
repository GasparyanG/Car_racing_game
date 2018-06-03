class Factory:
    def create(self, comparable_object, base_class, user):
        products = self.products_to_offer(base_class)

        for product in products:
            product = product(user)
            if product.is_used(comparable_object):
                return product

    def products_to_offer(self, base_class):
        products = base_class.__subclasses__()

        return products    