# Testing my twttr - 2

# Implement one or more functions that collectively test your implementation of shorten thoroughly,
# each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_twttr.py


# ===============================================================================


from twttr import shorten


def test_shorten():
    assert shorten("banana") == "bnn"
    assert shorten("bAnanA") == "bnn"
    assert shorten("banana1") == "bnn1"
    assert shorten("b.anana") == "b.nn"
