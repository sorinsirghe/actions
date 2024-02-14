from Functions.functions import random_number

# import pytest


def test_random():
    number = random_number()
    # test
    assert number % 2 == 0, "Number is not even!"
