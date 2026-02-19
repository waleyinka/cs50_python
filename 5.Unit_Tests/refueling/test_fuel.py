# Task: https://cs50.harvard.edu/python/psets/5/test_fuel/


import pytest
from fuel import convert, gauge

def test_valid_fractions():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_invalid_inputs():
    # Fractions outside 0..1, non-integers, floats, and negatives should error
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("-1/2")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_output():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"