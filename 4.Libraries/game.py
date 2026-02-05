# Guessing Game

# I’m thinking of a number between 1 and 100…

# What is it?
# It’s 50! But what if it were more random?

# In a file called game.py, implement a program that:

 # - Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
 # - Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
 # - Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        # - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        # - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        # - If the guess is the same as that integer, the program should output Just right! and exit.


# ===============================================================================


# import the random module to generate random numbers
import random 

# loop forever until the user enters a valid level
while True:
       try:
              # prompt the user for the difficulty level and convert input to integer
              level = int(input("Level: "))

              # ensure the level is a positive number and exit the loop
              if level > 0:
                     break  
     
       except ValueError:
              # if the input cannot be converted to an integer, re-prompt the user
              continue

# generate a random integer between 1 and the chosen level (inclusive)
secret_number = random.randint(1, level)

# loop forever to repeatedly ask the user for guesses
while True:
    try:
        # prompt the user for a guess and convert input to integer
        guess = int(input("Guess: "))

        # ignore guesses that are zero or negative
        if guess <= 0:
            continue

    except ValueError:
        # handle non-integer guesses
        continue  # re-prompt the user

    # compare the guess to the secret number, exit the loop once the correct number is guessed
    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too large!")
    else:
        print("Just right!")
        break 