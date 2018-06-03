class ImplementorOfBuying:
    def __init__(self, user):
        self.user = user

    def buy(self):
        raise NotImplementedError()


class BuyingStuff(ImplementorOfBuying):
    def buy(self):
        while True:
            # herre i have to offer products which i represented in market
            pass  