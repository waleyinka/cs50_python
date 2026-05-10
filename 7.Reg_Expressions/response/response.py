# Task: https://cs50.harvard.edu/python/psets/7/response/

import validators

def main():
    email = input("What is your email address? ")

    if validators.email(email):
        print("Valid")

    else:
        print("Invalid")

if __name__ == "__main__":
    main()
