class Franc:
    def __init__(self, amount) -> None:
        self._amount = amount

    # As we are using Python3 no need to implement __ne__ as __ne__ is calling __eq__.
    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return o._amount == self._amount
        return False


    def times(self, multiplier: int ):
        return Franc(multiplier * self._amount)