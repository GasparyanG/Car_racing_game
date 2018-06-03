from market_implementors import option_to_offer, categories_of_stuff_to_buy, factory_method


class ImplementorOfBuying:
    def __init__(self, user):
        self.user = user

    def buy(self):
        raise NotImplementedError()


class BuyingStuff(ImplementorOfBuying):
    def __init__(self, user):
        super().__init__(user)
        self.options = option_to_offer.OptionsToChoose()
        self.base_class = categories_of_stuff_to_buy.CategoriesOfStuff 
        self.factory = factory_method.Factory()

    def buy(self):
        while True:
            user_choice = self.options.offer(self.base_class)

            choosen_option = self.factory.create(user_choice, self.base_class, self.user)

            operation = choosen_option.buy()

            # after choosing leave option true will be returned! 
            if operation:
                print("Goodby {}, we hope you will come back leter to buy sth!".format(self.user.username))
                break