# Task: https://cs50.harvard.edu/python/psets/2/plates/

def main():
    plate = input("Plate: ").strip() #remove spaces
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    #first requirement - All vanity plates must start with at least two letters.
    if not s[0:2].isalpha():
        return False

    #second requirement - Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if not (2 <= len(s) <= 6):
        return False

    #third requirement - Numbers cannot be used in the middle of a plate; they must come at the end. The first number used cannot be a ‘0’.”
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0':
                return False
            if not s[i:].isdigit():
                return False
            break

    #fouth requirement - No periods, spaces, or punctuation marks are allowed..
    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()