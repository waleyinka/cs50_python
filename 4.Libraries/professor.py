# Little Professor

# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math
# problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4.
# If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.  

# If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem,
# the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

 # - Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
 # - Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. 
        # No need to support operations other than addition (+).
        # Note: The order in which you generate x and y matters. Your program should generate random numbers in x,
                # y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

 # - Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE
        # and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered
        # correctly after three tries, the program should output the correct answer.
 # - The program should ultimately output the user’s score: the number of correct answers out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
# and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:


# ===============================================================================


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
