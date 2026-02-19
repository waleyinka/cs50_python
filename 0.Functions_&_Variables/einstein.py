# Task: https://cs50.harvard.edu/python/psets/0/einstein/


def main():
    m = int(input("What's the mass of the object? "))
    c = int(300000000)
    E = m * square(c)
    print(f"Energy (E) = {E} joules")

def square(n):
    return pow(n, 2)

if __name__ == "__main__":
    main()