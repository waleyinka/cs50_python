# Task: https://cs50.harvard.edu/python/psets/2/twttr/


text = input("Enter your string here: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]

for i in text:
    if i not in vowels:
        print(i, end="")