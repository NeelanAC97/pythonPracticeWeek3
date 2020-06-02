import pytest
from Code import tuesday

def test_factorial_func1():
    assert tuesday.factorial_func(8) == 40320

def test_factorial_func2():
    assert tuesday.factorial_func(0) == print("The factorial of 0 is 1")

def test_factorial_func3():
    assert tuesday.factorial_func(-3) == print("Sorry, factorial does not exist for negative numbers")