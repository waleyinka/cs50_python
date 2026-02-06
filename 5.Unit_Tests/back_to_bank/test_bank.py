# Back to the Bank

# Implement three or more functions that collectively test your implementation of value thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:

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