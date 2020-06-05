import pytest
from Code.list2_sum13 import sum13

def test_sum13_1():
    assert sum13([1, 2, 2, 1]) == 6

def test_sum13_2():
    assert sum13([1, 1]) == 2

def test_sum13_3():
    assert sum13([1, 2, 2, 1, 13]) == 6