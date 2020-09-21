from src.money import Money

class Franc(Money):
    def __init__(self, amount) -> None:
        super(Franc, self).__init__(amount)

    def times(self, multiplier: int):
        return Franc(multiplier * self._amount)