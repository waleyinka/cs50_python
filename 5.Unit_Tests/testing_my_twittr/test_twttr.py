# Task: https://cs50.harvard.edu/python/psets/5/test_twttr/

from twttr import shorten

def test_shorten():
    assert shorten("banana") == "bnn"
    assert shorten("bAnanA") == "bnn"
    assert shorten("banana1") == "bnn1"
    assert shorten("b.anana") == "b.nn"
