from src.mdr import Mdr
from typing import Type

class Dollar:
    def __init__(self, amount) -> None:
        self.amount = amount

    def times(self, multiplier: int ):
        return Dollar(multiplier * self.amount)