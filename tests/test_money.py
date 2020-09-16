import sys
#sys.path.append("/Users/mortician/Projects/tdd_by_example/src")
#print(sys.path)
from tests.toto import Tata
print(Tata)
from src.money import Dollar


def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount