
class Money:
    def __init__(self, amount, currency) -> None:
        self._amount = amount
        self._currency = currency

    @property
    def currency(self):
        return self._currency

    # As we are using Python3 no need to implement __ne__ as __ne__ is calling __eq__.
    def __eq__(self, stranger: object) -> bool:
        return stranger._amount == self._amount and stranger.currency == self.currency
    
    def times(self, multiplier: int):
        return Money(multiplier * self._amount, self.currency)

    def dollar(amount: int):
        return Money(amount, "USD")

    def franc(amount: int):
        return Money(amount, "CHF")