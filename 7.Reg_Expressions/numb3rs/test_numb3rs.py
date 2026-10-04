# Task: https://cs50.harvard.edu/python/psets/7/numb3rs/

from numb3rs import validate


def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True


def test_invalid_range():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("300.1.1.1") == False


def test_invalid_format():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("cat") == False


def test_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("01.2.3.4") == False