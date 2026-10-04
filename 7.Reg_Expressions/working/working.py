# Task: https://cs50.harvard.edu/python/psets/7/working/

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):

    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_period = match.group(3)

    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_period = match.group(6)

    # Validate hours
    if not (1 <= start_hour <= 12):
        raise ValueError

    if not (1 <= end_hour <= 12):
        raise ValueError

    # Validate minutes
    if not (0 <= start_minute <= 59):
        raise ValueError

    if not (0 <= end_minute <= 59):
        raise ValueError

    # Convert start time
    if start_period == "AM":
        if start_hour == 12:
            start_hour = 0

    elif start_period == "PM":
        if start_hour != 12:
            start_hour += 12

    # Convert end time
    if end_period == "AM":
        if end_hour == 12:
            end_hour = 0

    elif end_period == "PM":
        if end_hour != 12:
            end_hour += 12

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

if __name__ == "__main__":
    main()