# Task: https://cs50.harvard.edu/python/psets/8/seasons/

from datetime import date

from seasons import calculate_minutes, minutes_to_words


def test_calculate_minutes_normal_year():
    birth_date = date(2021, 1, 1)
    today = date(2022, 1, 1)

    diff = today - birth_date

    assert calculate_minutes(diff) == 525600


def test_calculate_minutes_leap_year():
    birth_date = date(2020, 1, 1)
    today = date(2021, 1, 1)

    diff = today - birth_date

    assert calculate_minutes(diff) == 527040


def test_calculate_minutes_leap_day():
    birth_date = date(2020, 2, 28)
    today = date(2020, 3, 1)

    diff = today - birth_date

    assert calculate_minutes(diff) == 2880


def test_minutes_to_words():
    assert(
        minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    )


def test_minutes_to_words_leap_year():
    assert(
        minutes_to_words(527040) == "Five hundred twenty-seven thousand forty"
    )


def test_minutes_to_words_no_and():
    result = minutes_to_words(525600)

    assert " and " not in result.lower()






"""
from datetime import date

import pytest

from seasons import parse_date, minutes_between, minutes_to_words


def test_parse_date_valid():
    assert parse_date("1999-01-01") == date(1999, 1, 1)
    assert parse_date("2020-02-29") == date(2020, 2, 29)


def test_parse_date_wrong_format():
    for bad in ["January 1, 1999", "1999/01/01", "1999-1-1", "19990101", "cat", ""]:
        with pytest.raises(ValueError):
            parse_date(bad)


def test_parse_date_impossible_date():
    for bad in ["2023-02-30", "2023-13-01", "2021-02-29", "2023-00-10"]:
        with pytest.raises(ValueError):
            parse_date(bad)


def test_minutes_between():
    assert minutes_between(date(2021, 1, 1), date(2022, 1, 1)) == 525600
    assert minutes_between(date(2020, 1, 1), date(2021, 1, 1)) == 527040  # leap year
    assert minutes_between(date(2021, 1, 1), date(2023, 1, 1)) == 1051200
    assert minutes_between(date(2000, 1, 1), date(2000, 1, 1)) == 0


def test_minutes_between_future():
    with pytest.raises(ValueError):
        minutes_between(date(2030, 1, 1), date(2020, 1, 1))


def test_minutes_to_words():
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_to_words(527040) == "Five hundred twenty-seven thousand forty minutes"
    assert minutes_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"
    assert minutes_to_words(1052640) == "One million, fifty-two thousand, six hundred forty minutes"


def test_minutes_to_words_no_and():
    assert " and " not in minutes_to_words(1051200)
    assert " and " not in minutes_to_words(10512000)
"""
