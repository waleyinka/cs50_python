# Task: https://cs50.harvard.edu/python/psets/5/test_plates/


import sys

def main():
    # Read plate, remove leading/trailing whitespace
    plate = input("Plate: ").strip()

    print("Valid" if is_valid(plate) else "Invalid")

def is_valid(s: str) -> bool:
    # Rule 1: length must be between 2 and 6 inclusive
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: first two characters must be letters
    if not s[:2].isalpha():
        return False

    # Rule 3: only letters and numbers allowed (no spaces or punctuation)
    if not s.isalnum():
        return False

    # Rule 4 and 5:
    # Once numbers start, no letters may appear after.
    # The first number cannot be 0.
    seen_digit = False

    for char in s:
        if char.isdigit():
            if not seen_digit:
                # This is the first digit we have encountered
                seen_digit = True
                if char == "0":
                    return False
        else:
            # char is a letter
            if seen_digit:
                return False

    return True

if __name__ == "__main__":
    main()