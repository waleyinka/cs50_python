#[TASK 1 - INDOOR VOICE]

#In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input
# in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the
# user explicitly, as by passing a str of your own as an argument to input.

value = input("What's your input value? ").lower()
print(value)




#[TASK 2 - PLAYBACK SPEED]

#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that
# same input, replacing each space with ... (i.e., three periods).

text = input("Enter a sample text")
rep_text = text.replace(" " , "...")
print(rep_text)




#[TASK 3 - MAKING FACES]

#In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with
# any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁
#(otherwise known as a slightly frowning face). All other text should be returned unchanged.

#Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input,
#and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as
#an argument to input. Be sure to call main at the bottom of your file.

def convert(text):
     return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
     sample_text = input("Input sample text: ")
     print(convert(sample_text))

main()



#[TASK 4 - EINSTEIN]

#In a file called einstein.py, implement a program in Python that prompts the user for mass as an
#integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
#Assume that the user will input an integer.

def main():
    m = int(input("What's the mass of the object? "))
    c = int(300000000)
    E = m * square(c)
    print(f"Energy (E) = {E} joules")

def square(n):
    return pow(n, 2)

main()



#[TASK 5 - TIP CALCULATOR]

#In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
#typically an amount equal to 15% or more of your meal’s cost.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # TODO
    return float(d.lstrip("$"))

def percent_to_float(p):
    # TODO
    return float(p.rstrip("%")) / 100

main()