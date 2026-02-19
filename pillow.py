# https://cs50.harvard.edu/python/shorts/pillow/

# PIL (Pillow) is a Python library for opening, manipulating, and saving many different image file formats.
from PIL import Image, ImageFilter

def main():
    # Open an image file
    with Image.open('images/in.png') as img:
        # Display the image
        # img.show()
        
        # Perform some operations on the image
        img = img.rotate(45)    # Rotate the image by 45 degrees
        img = img.filter(ImageFilter.BLUR)  # Apply a blur filter to the image
        
        # Print image format, size, and mode
        print(f'Format: {img.format}')
        print(f'Size: {img.size}')
        print(f'Mode: {img.mode}')
        
        # Save the image output to a new file
        img.save('images/out.jpg')

if __name__ == "__main__":
    main()