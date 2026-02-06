# Testing my twttr - 1

# Reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input
# and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


# ===============================================================================


def main():
    # Prompt the user for input and shorten the string
    text = shorten(input("Enter your string here: "))
    print(text)


def shorten(word):
    # List to collect non-vowel characters
    result = []

    # Define vowels in lowercase for comparison
    vowels = ["a", "e", "i", "o", "u"]

    for char in word:
        # Convert character to lowercase for case-insensitive comparison
        if char.casefold() in vowels:
            # Skip vowels
            continue
        else:
            # Preserve original character (including case, numbers, punctuation)
            result.append(char)

    # Join the list into a single string
    output = "".join(result)

    return output


if __name__ == "__main__":
    main()
