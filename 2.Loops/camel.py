# CAMEL CASE

# Implement a program that prompts the user for the name of a variable in camel case and outputs the
# corresponding name in snake case. Assume that the user’s input will indeed be in camel case.


# ===============================================================================


# accept camelCase input from users
camel_case = input("Enter you came case variable here: ")

# check if character in variable in lower the print character,
# other append _ and print charatcer in lowercase

for c in camel_case:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")