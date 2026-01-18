# JUST SETTING UP MY TWTTR

#Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels
#(A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

text = input("Enter your string here: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

for i in text:
    if i not in vowels:
        print(i, end="")