# Frank, Ian and Glen’s Letters

# FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

# _ _ _          _   _     _
# | (_) | _____  | |_| |__ (_)___
# | | | |/ / _ \ | __| '_ \| / __|
# | | |   <  __/ | |_| | | | \__ \
# |_|_|_|\_\___|  \__|_| |_|_|___/

# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

 # - Expects zero or two command-line arguments:
        # - Zero if the user would like to output text in a random font.
        # - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
        #   and the second of the two should be the name of the font.
 # - Prompts the user for a str of text.
 # - Outputs that text in the desired font.

# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
# the program should exit via sys.exit with an error message.


# ===============================================================================


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