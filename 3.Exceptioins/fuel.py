# Task: https://cs50.harvard.edu/python/psets/3/fuel/

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

if __name__ == "__main__":
    main()