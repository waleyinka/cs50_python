# Task: https://cs50.harvard.edu/python/psets/5/test_plates/

from plates import is_valid

def test_length():
    # Too short and too long
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False

    # Boundary valid lengths
    assert is_valid("AB") is True
    assert is_valid("ABCDEF") is True

def test_starting_letters():
    # Must begin with two letters
    assert is_valid("1A") is False
    assert is_valid("A1") is False
    assert is_valid("AB") is True

def test_only_alphanumeric():
    # No spaces or punctuation
    assert is_valid("AB CD") is False
    assert is_valid("AB.CD") is False
    assert is_valid("AB123") is True

def test_number_rules():
    # Numbers, if present, must be at the end
    assert is_valid("AB12CD") is False
    assert is_valid("AB1C") is False
    assert is_valid("ABC1") is True
    assert is_valid("AB123") is True

    # First digit cannot be 0
    assert is_valid("AB012") is False
    assert is_valid("AB0") is False
    assert is_valid("AB101") is True
