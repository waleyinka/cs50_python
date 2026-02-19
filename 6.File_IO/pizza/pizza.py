# Task: https://cs50.harvard.edu/python/psets/6/pizza/

import sys
import csv
from tabulate import tabulate 

def main():  
    # Validate argument count: program name + exactly one CSV path     
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
        
    csv_path = sys.argv[1]
    
    # Validate file extension
    if not csv_path.endswith(".csv"):
        sys.exit("Not a CSV file")
        
    try:
        # Read rows while the file is open (reader depends on the open file handle)
        with open(csv_path, 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            row_list = list(reader) 
        
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    if not row_list:
        sys.exit("File does not exist")
    
    # Print table using the first row as headers
    # print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    print(tabulate(row_list[1:], headers=row_list[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
    



