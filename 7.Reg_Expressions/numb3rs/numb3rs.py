# Task: https://cs50.harvard.edu/python/psets/7/numb3rs/

import re

# Regular expression pattern to validate IPv4 addresses
pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"

def validate(ip):
    return re.match(pattern, ip) is not None

def main():
    print(validate(input("IPv4 Address: ")))

if __name__ == "__main__":
    main()