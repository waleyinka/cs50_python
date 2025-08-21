### Task 4.
> [!NOTE]
> In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main():
    m = int(input("What's the mass of the object? "))
    c = int(300000000)
    E = m * square(c)
    print(f"Energy (E) = {E} joules")

def square(n):
    return pow(n, 2)

main()

