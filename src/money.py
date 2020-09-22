
class Money:
    def __init__(self, amount, currency) -> None:
        self._amount = amount
        self._currency = currency

    @property
    def currency(self):
        return self._currency

    # As we are using Python3 no need to implement __ne__ as __ne__ is calling __eq__.
    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return o._amount == self._amount
        return False
    
    def dollar(amount: int):
        from src.dollar import Dollar

        return Dollar(amount)

    def franc(amount: int):
        from src.franc import Franc

        return Franc(amount)