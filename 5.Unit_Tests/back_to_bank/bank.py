# Task: https://cs50.harvard.edu/python/psets/5/back_to_bank/

def main():
    # Prompt the user for a greeting, normalizing whitespace and casing early
    greeting = input("Enter your greeting here: ").strip().lower()

    # Determine the monetary value associated with the greeting
    amount = value(greeting)

    # Output the result
    print(amount)

def value(greeting: str) -> int:
    """
    Returns a monetary value based on the greeting:
    - $0 if the greeting starts with 'hello'
    - $20 if the greeting starts with 'h' (but not 'hello')
    - $100 otherwise
    """
    # Normalize input to ensure consistent comparisons
    greeting = greeting.lower()

    # Most specific condition first
    if greeting.startswith("hello"):
        return 0

    # Less specific condition next
    elif greeting.startswith("h"):
        return 20

    # Default case for all other greetings
    else:
        return 100

if __name__ == "__main__":
    main()