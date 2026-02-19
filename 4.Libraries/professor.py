# Task: https://cs50.harvard.edu/python/psets/4/professor/


import random

def main():
    # Prompt the user for a difficulty level (1, 2, or 3)
    level = get_level()

    # Track how many questions the user answers correctly
    score = 0

    # Generate and ask 10 questions
    for _ in range(10):

        # Generate two random integers based on the chosen level
        x = generate_integer(level)
        y = generate_integer(level)

        # Calculate correct answer
        correct_answer = x + y

        # Track the number of attempts for the current question
        attempts = 0

        while attempts < 3:
            try:
                # Prompt the user and attempt to convert input to an integer
                user_answer = int(input(f"{x} + {y} = "))

                # If the user's answer is correct, award a point and move on to the next question
                if user_answer == correct_answer:
                    score += 1
                    break
                
                # If the user's answer is incorrect, print "EEE" and count this as an attempt
                else:
                    print("EEE")
                    attempts += 1 

            # Non-integer input (letters, symbols, empty input) should be treated as an incorrect answer
            except ValueError:
                print("EEE")
                attempts += 1

        # If the user used all 3 attempts without success
        # reveal the correct answer before continuing
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    # Output the numeric score
    print(score)

def get_level():
    # Continuously prompt until a valid level is provided
    while True:
        try:
            # Convert user input to integer
            level = int(input("Level: "))

            if level in (1, 2, 3):
                return level

        # If conversion fails, ignore the input and prompt again
        except ValueError:
            continue

def generate_integer(level):
    # Generate a random integer based on difficulty level

    # Single-digit numbers (easy)
    if level == 1:
        return random.randint(0, 9)

    # Two-digit numbers (medium)
    elif level == 2:
        return random.randint(10, 99)

    # Three-digit numbers (hard)
    elif level == 3:
        return random.randint(100, 999)

    raise ValueError("Invalid level")


if __name__ == "__main__":
    main()