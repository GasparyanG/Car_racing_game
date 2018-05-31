class ImplementorOfBuying:
    def __init__(self, user):
        self.user = user

    def buy(self):
        raise NotImplementedError()


class BuyingStuff(ImplementorOfBuying):
    def buy(self):
        while True:
            pass  