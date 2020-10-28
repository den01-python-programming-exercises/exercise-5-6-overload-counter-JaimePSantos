import pytest
from src.counter import Counter

def test_exercise():
    counter = Counter(10)
    assert counter.value == 10

    counter.increase(5)
    assert counter.value == 15

    counter.decrease(10)
    assert counter.value == 5

    counter.increase()
    assert counter.value == 6

    counter.decrease()
    assert counter.value == 5
