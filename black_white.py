"""
Creates a greyscale image from a given image and displays it alongside the original image.
"""

# The essence of this program is now in image_transform.py.  For this reason this file is no longer needed.

import argparse
import greyscale
from cImage import *

def black_white(image):
    """
    Takes an image and creates a black-and-white image.
    :param image: The image manipulated
    :return: Nothing.  Shows the two images in a window side-by-side
    """

    im = FileImage(image)
    width = im.getWidth()
    height = im.getHeight()

    display = ImageWin("Normal and Black and White", 2*width, height)

    def no_red_pix(pix):
        """
        Inputs a pixel and returns it with no red
        :param pix: The pixel to remove red from
        :return: A non-red pixel
        """

        green = pix.getGreen()
        blue = pix.getBlue()
        redless = Pixel(0, green, blue)

        return redless

    redless_im = EmptyImage(width, height)

    for i in range(width):
        for j in range(height):
            pixel = im.getPixel(i, j)
            redless = no_red_pix(pixel)
            redless_im.setPixel(i, j, redless)

    redless_im.setPosition(width+1,0)
    im.draw(display)
    redless_im.draw(display)

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
    no_red(image)


if __name__ == "__main__":
    main()
