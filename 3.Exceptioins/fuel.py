# Fuel Guage

# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
# and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs,
# as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is
# essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any
# exceptions like ValueError or ZeroDivisionError.

def main():
    x, y = get_input()
    result = calculate_percentage(x, y)
    print(result)


def get_input():
    while True:
        try:
            x_input, y_input = input("Enter a fraction here: ").split(sep = "/")
            x = int(x_input)
            y = int(y_input)

            if y == 0:
                raise ZeroDivisionError("Denominator can not be zero")
            if x > y:
                raise ValueError("Numerator can not be greater than denominator")
            if x < 0 or y < 0:
                raise ValueError("Both numerator and denominator must be positive")

            return x, y

        except(ValueError, ZeroDivisionError):
            print("invalid input, try again")


def calculate_percentage(x,y):
    percentage = round(x / y * 100)

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


main()