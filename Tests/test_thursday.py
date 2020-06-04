import pytest
from Code.thursday import count_vowels

def test_count_vowels1():
    assert count_vowels("abcdefghijklmnopqrstuvwxyz") == 5

def test_count_vowels2():
    assert count_vowels("fyegbeiaGWBAAEEORIJRGRO") == 11
