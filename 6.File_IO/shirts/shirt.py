# Task: https://cs50.harvard.edu/python/psets/6/shirt/

import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    allowed_exts = {".jpg", ".jpeg", ".png"}

    if input_ext not in allowed_exts or output_ext not in allowed_exts:
        sys.exit("invalid input")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        shirt_image = Image.open('shirt.png')
        shirt_size = shirt_image.size
        photo = Image.open(input_path)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    fitted = ImageOps.fit(photo, shirt_size)
    fitted.paste(shirt_image, (0, 0), shirt_image)
    fitted.save(output_path)

if __name__ == "__main__":
    main()