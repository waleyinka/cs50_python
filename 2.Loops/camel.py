# Task: https://cs50.harvard.edu/python/psets/2/camel/


# accept camelCase input from users
camel_case = input("Enter you came case variable here: ")

# check if character in variable in lower the print character,
# other append _ and print charatcer in lowercase

for c in camel_case:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")