from src.money import Money

class Dollar(Money):
    def __init__(self, amount) -> None:
        super(Dollar, self).__init__(amount)

    def times(self, multiplier: int ):
        return Dollar(multiplier * self._amount)