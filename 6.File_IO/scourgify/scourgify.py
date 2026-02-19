# Task: https://cs50.harvard.edu/python/psets/6/scourgify/

import sys
import csv

def main():
    """
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
        
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    """
    
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        with open(input_path, "r", encoding="utf-8", newline="") as input_file, \
            open(output_path, "w", encoding="utf-8", newline="") as output_file:
                
                reader = csv.DictReader(input_file)
                
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()
                
                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
            
                    cleaned_row = {
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": house.strip()
                    }
            
                    writer.writerow(cleaned_row)
    
    except(FileNotFoundError, PermissionError, OSError):
        sys.exit("Couldt not read input file")
    
    except csv.Error:
        sys.exit("CSV error")
    
            
if __name__ == "__main__":
    main()
        