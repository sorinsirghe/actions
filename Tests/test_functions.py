from Functions.functions import random_number

# import pytest

# test
def test_random():
    number = random_number()

    assert number % 2 == 0, "Number is not even!"
