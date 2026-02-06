# Back to the Bank

# Reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns an int,
# namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the
# string passed to the value function will not contain any leading spaces. Only main should call print.


# ===============================================================================


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