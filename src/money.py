from src.mdr import Mdr

class Dollar:
    def __init__(self, amount) -> None:
        self.amount = amount

    def times(self, multiplier):
        self.amount *=  multiplier