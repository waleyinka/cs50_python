# Task: https://cs50.harvard.edu/python/psets/5/test_bank/

from bank import value

def test_hello():
    # Any greeting starting with "hello" should return 0
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello there") == 0

def test_h():
    # Greetings starting with 'h' but not 'hello' return 20
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Howdy") == 20

def test_non_h():
    # All other greetings return 100
    assert value("good morning") == 100
    assert value("yo") == 100
    assert value("What's up") == 100