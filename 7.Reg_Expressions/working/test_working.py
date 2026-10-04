# Task: https://cs50.harvard.edu/python/psets/7/working/

import pytest
from working import convert

def test_valid_hour():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"

def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM-5PM")