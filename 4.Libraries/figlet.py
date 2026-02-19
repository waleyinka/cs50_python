# Task: https://cs50.harvard.edu/python/psets/4/figlet/

from pyfiglet import Figlet
import sys
import random

def main():
       # Create an instance of the Figlet class.
       figlet = Figlet()

       # Get a list of available fonts
       available_fonts = figlet.getFonts()

       # Determine how many arguments were provided.
       argc = len(sys.argv)

       # Case 1: No additional arguments were provided.
       if argc == 1:
              chosen_font = random.choice(available_fonts)

       # Case 2: Exactly two additional arguments were provided.
       elif argc == 3:
              # Extract the flag (e.g., -f or --font)
              flag = sys.argv[1]
              
              # Extract the font name specified by the user
              font_name = sys.argv[2]

              # Validate that the provided flag is one of the supported options.
              if flag not in ("-f", "--font"):
                     sys.exit("Invalid usage: first argument must be -f or --font")

              # Validate that the requested font actually exists.
              if font_name not in available_fonts:
                     sys.exit("Invalid font: font name not supported")

              chosen_font = font_name

       # Any other number of arguments is invalid.
       else:
              sys.exit("Invalid usage: expected 0 or 2 arguments")

       # Prompt the user for the text they want to render.
       text_input = input("Input: ")

       # Configure the Figlet instance to use the chosen font.
       figlet.setFont(font=chosen_font)

       # Render the user's input text as ASCII art using the selected font.
       rendered_text = figlet.renderText(text_input)

       # Output the rendered ASCII art to the terminal.
       print(rendered_text)

if __name__ == "__main__":
    main()