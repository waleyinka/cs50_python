# Task: https://cs50.harvard.edu/python/psets/4/adieu/

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

if __name__ == "__main__":
      main()