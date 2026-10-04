# Task: https://cs50.harvard.edu/python/psets/8/seasons/

from datetime import date
import sys
import inflect


def get_birth_date():
    """Prompt the user for their date of birth and return it as a date object."""
    date_of_birth = input("Please enter your date of birth..... ")

    try:
        return date.fromisoformat(date_of_birth)
    except ValueError:
        sys.exit("Invalid date")


def calculate_minutes(diff):
    """Calculate the total number of minutes in the given timedelta object."""
    minutes = diff.days * 24 * 60

    return minutes


def minutes_to_words(minutes):
    """Convert a number of minutes into words using the inflect library."""
    engine = inflect.engine()

    words = engine.number_to_words(minutes)
    words = words.replace(" and ", " ")

    return words.capitalize()


def main():
    """Main function to calculate and display the number of minutes since the user's birth date in words."""
    birth_date = get_birth_date()
    today = date.today()

    diff = today - birth_date

    minutes = calculate_minutes(diff)
    words = minutes_to_words(minutes)

    print(f"{words} minutes")


if __name__ == "__main__":
    main()



"""
from datetime import date
import re
import sys

import inflect


p = inflect.engine()


def main():
    try:
        birth = parse_date(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    minutes = minutes_between(birth, date.today())
    print(minutes_to_words(minutes))


def parse_date(s):
    """Return a date from a strict YYYY-MM-DD string, else raise ValueError."""
    s = s.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        raise ValueError("Invalid format")
    # fromisoformat raises ValueError for impossible dates like 2023-02-30
    return date.fromisoformat(s)


def minutes_between(start, end):
    """Return whole minutes from start to end (both treated as midnight)."""
    if start > end:
        raise ValueError("Date is in the future")
    return (end - start).days * 24 * 60


def minutes_to_words(minutes):
    """Return e.g. 'Five hundred twenty-five thousand, six hundred minutes'."""
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
"""