# Task: https://cs50.harvard.edu/python/psets/1/interpreter/

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

if __name__ == "__main__":
    main()