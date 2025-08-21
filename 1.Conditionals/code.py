#[TASK 1 - DEEP THOUGHTS]

#Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or
#(case-insensitively) forty-two or forty two. Otherwise output No.

user_answer = input("The Answer to the Great Question of Life is? ").strip().lower()

match user_answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")




#[TASK 2 - HOME FEDERAL SAVINGS BANK]

#Implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”),
#output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    greeting = input("Enter your greeting here: ").strip().lower()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()




#[TASK 3 - FILE EXTENSION]

#In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
# case-insensitively, in any of these suffixes:
#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

def main():

    file_name = input("What is the name of your file? ").strip().lower()

    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpeg") or file_name.endswith(".jpg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()




#[TASK 4 - MATH INTERPRETER]

#In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a
#floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space
#between y and z, wherein:
#x is an integer
#y is +, -, *, or /
#z is an integer
#For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

def main():

    expression = input("Enter your arithmetic expression: ")

    x, y, z = expression.split(" ")

    if y == "+":
        calculation = int(x) + int(z)
        print(f"{calculation:.1f}")
    elif y == "-":
        calculation = int(x) - int(z)
        print(f"{calculation:.1f}")
    elif y == "/":
        calculation = int(x) / int(z)
        print(f"{calculation:.1f}")
    elif y == "*":
        calculation = int(x) * int(z)
        print(f"{calculation:.1f}")

main()



#[TASK 5 - MEAL TIME]

#Implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t
#output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
#For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

#Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the
#corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():

    user_input = input("What time is it? ").strip()

    meal_time = convert(user_input)

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    if 18.0 <= meal_time <= 19.0:
        print("dinner time")

def convert(time):

    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes) / 60

    return hours + minutes

if __name__ == "__main__":
    main()
