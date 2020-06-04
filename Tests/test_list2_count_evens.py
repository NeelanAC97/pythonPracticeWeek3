import pytest
from Code.list2_count_evens import count_evens

def test_count_evens1():
    assert count_evens([2, 1, 2, 3, 4]) == 3

def test_count_evens2():
    assert count_evens([2,2,0]) == 3

def test_count_evens3():
    assert count_evens([1,3,5]) == 0