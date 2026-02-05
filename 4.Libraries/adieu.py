# Adieu, Adieu

# In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

 # Adieu, adieu, to yieu and yieu and yieu

# Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

 # Adieu, adieu, to yieu, yieu, and yieu

# To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user
# will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and,
# and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

 # Adieu, adieu, to Liesl
 # Adieu, adieu, to Liesl and Friedrich
 # Adieu, adieu, to Liesl, Friedrich, and Louisa
 # Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
 # Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
 # Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
 # Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


# ===============================================================================


# Import the inflect library for proper grammatical joins (e.g., commas and 'and')
import inflect


def main():
    # Create an inflect engine instance to handle pluralization and list joining
    p = inflect.engine()
    
    # Initialize an empty list to store all entered names
    names = []

    # Continuously prompt the user for names until an EOF signal is received
    while True:
        try:
            # Prompt for a name and remove leading/trailing whitespace
            name = input("Name: ").strip()
            
            # Only add the name if the user actually entered something
            if name:
                names.append(name)
                
        except EOFError:
            # Handle end-of-file input (Ctrl+D on Unix, Ctrl+Z then Enter on Windows)
            # Print a newline for clean output formatting
            print()
            break
    
    # Join the list of names into a human-readable string
    # Examples:
    # ["Alice"] -> "Alice"
    # ["Alice", "Bob"] -> "Alice and Bob"
    # ["Alice", "Bob", "Charlie"] -> "Alice, Bob, and Charlie"
    output = p.join(names)

    # Print the farewell message using the formatted list of names
    print(f"Adieu, adieu, to {output}")


# Ensure main() runs only when this file is executed directly,
# not when it is imported as a module
if __name__ == "__main__":
      main()