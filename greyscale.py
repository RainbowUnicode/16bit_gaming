"""
Creates a greyscale image from a given image and displays it alongside the original image.
"""

import argparse
from cImage import *

def greyscale(image):
    """
    Takes an image and prints the image and its greyscale version side-by-side.
    :param image: The image used to produce a negative
    :return: Nothing.  Shows image and its negative in a window side-by-side
    """

    im = FileImage(image)
    width = im.getWidth()
    height = im.getHeight()

    display = ImageWin("Normal and Greyscale", 2*width, height)

    def grey_pixel(pix):
        """
        Inputs a pixel and returns its greyscale pixel
        :param pix: The pixel to convert to greyscale
        :return: A grey pixel
        """

        red = pix.getRed()
        green = pix.getGreen()
        blue = pix.getBlue()
        grey = (red+green+blue)//3
        gry_pixel = Pixel(grey, grey, grey)

        return gry_pixel

    grey_im = EmptyImage(width, height)

    for i in range(width):
        for j in range(height):
            pixel = im.getPixel(i, j)
            grey_px = grey_pixel(pixel)
            grey_im.setPixel(i, j, grey_px)

    grey_im.setPosition(width+1,0)
    im.draw(display)
    grey_im.draw(display)

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
    greyscale(image)


if __name__ == "__main__":
    main()
