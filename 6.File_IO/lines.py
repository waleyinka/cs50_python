# Task: https://cs50.harvard.edu/x/2024/psets/6/file-io/lines/

import sys

def main():
    """Count lines of code in a Python file, excluding blanks and comments."""
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")
    
    """    
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    """
    
    filename = sys.argv[1]
    
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")
        
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            loc = count_lines(file)
        
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    print(loc)
    
    
def count_lines(file):
    """Return number of lines of actual code.

    A valid LOC is any line that:
    - is not blank
    - does not start with '#' after optional whitespace

    Docstrings are counted because they are executable string expressions.

    Args:
        file: An open file object to read from.

    Returns:
        Integer number of lines of code.
    """
    line_count = 0
    
    for line in file:
        
        stripped = line.strip()
        
        # Ignore blank or whitespace-only lines
        if stripped == "":
            continue
        
        # Ignore comment lines
        if stripped.startswith("#"):
            continue
        
        # Count everything else as line of code
        else:
            line_count += 1
    
    return line_count
    

if __name__ == "__main__":
    main()
        
        

