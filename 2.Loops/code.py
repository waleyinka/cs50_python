#[CAMEL CASE]

#Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
#Assume that the user’s input will indeed be in camel case.

camel_case = input("Enter you came case variable here: ") #accept camelCase input from users

for c in camel_case:    #check if character in variable in lower the print character, other append _ and print charatcer in lowercase
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")





#[COKE MACHINE]

#Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user
#has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers,
#and ignore any integer that isn’t an accepted denomination.

def main():
     amount_due = 50

     while amount_due > 0:
          print(f"Amount Due: {amount_due}")

          coin = get_coin()

          if coin == 0:
               print("Invalid amount! Please insert 5, 10 or 25\r\nInsert coin (5, 10, 25):")
               continue
          amount_due -= coin

          if amount_due > 0:
               print(f"Amount due: {amount_due}")

     print(f"Change Owed: {abs(amount_due)}")

def get_coin():
     amount_inserted = int(input("Insert coin (5, 10, 25):"))
     if amount_inserted in [5, 10, 25]:
          return amount_inserted
     else:
          return 0

main()





#[JUST SETTING UP MY TWTTR]

#Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
#whether inputted in uppercase or lowercase.

text = input("Enter your string here: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

for i in text:
    if i not in vowels:
        print(i, end="")





#[VANITY PLATE]

#Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any
#letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it
#does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement)..

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

main()





#[NUTRITION FACTS]

#Implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit,
#per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster
#(e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

fruits = {
    "Apple" : 130,
    "Avocado" : 50,
    "Banana" : 110,
    "Cantaloupe" : 50,
    "Grapefruit" : 60,
    "Grapes" : 90,
    "Honeydrew Melon" : 50,
    "Kiwifruit" : 90,
    "Lemon" : 15,
    "Lime" : 20,
    "Nectarine" : 60,
    "Orange" : 80,
    "Peach" : 60,
    "Pear" : 100,
    "Pineapple" : 50,
    "Plums" : 70,
    "Strawberries" : 50,
    "Sweet Cherries" : 100,
    "Tangerine" : 50,
    "Watermelon" : 80
}

fruit_name = input("Enter the name of your fruit: ").title()

if fruit_name in fruits:
    print(fruits[fruit_name])
