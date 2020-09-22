from src.money import Money

class Dollar(Money):
    def __init__(self, amount) -> None:
        super(Dollar, self).__init__(amount, "USD")

    def times(self, multiplier: int ):
        return Money.dollar(multiplier * self._amount)