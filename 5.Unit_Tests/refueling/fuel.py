# Task: https://cs50.harvard.edu/python/psets/5/test_fuel/


def main():
    while True:
        try:
            fraction = input("Enter a fraction here: ")

            percentage = convert(fraction)

            print(gauge(percentage))
            break

        except (ValueError, ZeroDivisionError):
            # Any invalid fraction input should just re-prompt the user
            continue

def convert(fraction: str) -> int:
    """Convert a fraction string into a whole-number percentage.

    Args:
        fraction: A string in the form "X/Y", where X and Y are integers.

    Returns:
        An integer percentage rounded to the nearest whole number.

    Raises:
        ValueError: If fraction is not in "X/Y" form, contains non-integers,
            or represents a value outside the range 0..1 (e.g., "2/1", "-1/2").
        ZeroDivisionError: If the denominator is 0 (e.g., "1/0").
    """
    # Split input by "/" into numerator and denominator strings
    x_str, y_str = fraction.split("/")

    # Convert both parts to integers; if conversion fails, raise ValueError
    try:
        x = int(x_str)
        y = int(y_str)
        
    except ValueError as exc:
        raise ValueError("Numerator and denominator must be integers") from exc

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    # Validate logical bounds: fraction must be between 0 and 1 inclusive
    if x < 0 or x > y:
        raise ValueError("Fraction must be between 0 and 1 inclusive")

    # Convert to percentage and round to nearest whole number
    return round((x / y) * 100)

def gauge(percentage: int) -> str:
    """Convert a percentage into a fuel gauge reading.

    Args:
        percentage: Integer percentage (typically 0..100).

    Returns:
        A string representing the gauge:
            "E" if percentage is 1 or less,
            "F" if percentage is 99 or more,
            otherwise "{percentage}%".
    """
    if percentage <= 1:
        return "E"
    
    if percentage >= 99:
        return "F"

    return f"{percentage}%"

if __name__ == "__main__":
    main()