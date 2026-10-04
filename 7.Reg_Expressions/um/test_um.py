# Task: https://cs50.harvard.edu/python/psets/7/um/

from um import count

def test_single_um():
    assert count("um") == 1

def test_case_insensitive():
    assert count("Um, thanks") == 1
    assert count("UM") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3

def test_substrings_not_counted():
    assert count("yummy album umbrella") == 0

def test_punctutuation():
    assert count("Hello, um... world!") == 1