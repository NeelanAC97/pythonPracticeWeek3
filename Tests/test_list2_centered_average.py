import pytest
from Code.list2_centered_average import centered_average

def test_centered_average1():
    assert centered_average([1, 2, 3, 4, 100]) == 3

def test_centered_average2():
    assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5

def test_centered_average2():
    assert centered_average([-10, -4, -2, -4, -2, 0]) == -3