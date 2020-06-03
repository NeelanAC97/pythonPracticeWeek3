import pytest
from Code.wednesday import add_to_dictionary

def test_add_to_dictionary1():
    assert add_to_dictionary(5) == {1:1, 2:4, 3:9, 4:16, 5:25}