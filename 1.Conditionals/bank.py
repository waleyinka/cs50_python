# Task: https://cs50.harvard.edu/python/psets/1/bank/

def main():
    greeting = input("Enter your greeting here: ").strip().lower()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()