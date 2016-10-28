"""
Creates a negative of an image and displays it alongside that image.
"""

import argparse
from cImage import *

def negative(image):

    im = FileImage(image)
    width = im.getWidth()
    height = im.getHeight()

    display = ImageWin("Normal and Negative", 2*width, height)

    neg_im = EmptyImage(width, height)

    for i in range(width):
        for j in range(height):
            pixel = im.getPixel(i, j)
            negative_pixel = Pixel(255-pixel.getRed(), 255-pixel.getGreen(), 255-pixel.getBlue())
            neg_im.setPixel(i, j, negative_pixel)

    neg_im.setPosition(width+1,0)
    im.draw(display)
    neg_im.draw(display)

    display.exitOnClick()

def main():
    """
    collect command arguments and invoke negative()
    inputs:
        none, fetches arguments using argparse
    effects:
        calls negative()
    """
    parser = argparse.ArgumentParser(description="Displays a negative of the input image")
    parser.add_argument("image", type=str, help="Image to make into a negative")
    args = parser.parse_args()  # gets arguments from command line
    image = args.image
    negative(image)


if __name__ == "__main__":
    main()
