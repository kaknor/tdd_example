from src.money import Money

class Franc(Money):
    def __init__(self, amount) -> None:
        super(Franc, self).__init__(amount)

    # As we are using Python3 no need to implement __ne__ as __ne__ is calling __eq__.
    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return o._amount == self._amount
        return False


    def times(self, multiplier: int ):
        return Franc(multiplier * self._amount)