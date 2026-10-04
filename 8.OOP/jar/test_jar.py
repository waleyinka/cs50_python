# Task: https://cs50.harvard.edu/python/psets/8/jar/

import pytest

from jar import Jar

def test_init():
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0


def test_init_custom_capacity():
    jar = Jar(20)

    assert jar.capacity == 20
    assert jar.size == 0


def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(1)

    assert str(jar) == "🍪"

    jar.deposit(11)

    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    jar.deposit(3)

    assert jar.size == 3

    jar.deposit(2)

    assert jar.size == 5


def test_deposit_too_many():
    jar = Jar(5)

    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)

    assert jar.size == 3


def test_withdraw_too_many():
    jar = Jar()

    jar.deposit(3)

    with pytest.raises(ValueError):
        jar.withdraw(4)
