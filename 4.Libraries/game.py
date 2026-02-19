# Task: https://cs50.harvard.edu/python/psets/4/game/


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