# Task: https://cs50.harvard.edu/python/psets/0/faces/

def convert(text):
     return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
     sample_text = input("Input sample text: ")
     print(convert(sample_text))

if __name__ == "__main__":
     main()