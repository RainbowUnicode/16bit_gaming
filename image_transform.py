"""
Creates a negative of an image and displays it alongside that image.
"""

import argparse
from cImage import *


def negative(pixel):
    red = pixel.getRed()
    green = pixel.getGreen()
    blue = pixel.getBlue()
    new_pixel = Pixel(255 - red, 255 - green, 255 - blue)
    return new_pixel


def greyscale(pixel):
    red = pixel.getRed()
    green = pixel.getGreen()
    blue = pixel.getBlue()
    grey = (red + green + blue) // 3
    new_pixel = Pixel(grey, grey, grey)
    return new_pixel


def no_red(pixel):
    red = 0
    green = pixel.getGreen()
    blue = pixel.getBlue()
    new_pixel = Pixel(0, green, blue)
    return new_pixel


def no_green(pixel):
    red = pixel.getRed()
    blue = pixel.getBlue()
    new_pixel = Pixel(red, 0, blue)
    return new_pixel


def no_blue(pixel):
    red = pixel.getRed()
    green = pixel.getGreen()
    blue = pixel.getBlue()
    new_pixel = Pixel(red, green, 0)
    return new_pixel


def max_red(pixel):
    red = 255
    green = pixel.getGreen()
    blue = pixel.getBlue()
    new_pixel = Pixel(red, green, blue)
    return new_pixel


def max_green(pixel):
    red = pixel.getRed()
    green = 255
    blue = pixel.getBlue()
    new_pixel = Pixel(red, green, blue)
    return new_pixel

def max_blue(pixel):
    red = pixel.getRed()
    green = pixel.getGreen()
    blue = 255
    new_pixel = Pixel(red, green, blue)
    return new_pixel

def swirl(pixel):
    red = pixel.getRed()
    green = pixel.getGreen()
    blue = pixel.getBlue()
    new_pixel = Pixel(green, blue, red)
    return new_pixel


def transform_image(rgb_function, image):
    """
    Takes an image and applies the rgb_function to it
    :param rgb_function: The function transform applied to the image one pixel at a time
    :param image: The image to be transformed
    :return: The transformed image new_image
    """

    im = FileImage(image)
    width = im.getWidth()
    height = im.getHeight()
    new_im = EmptyImage(width, height)

    for i in range(width):
        for j in range(height):
            pixel = im.getPixel(i, j)
            new_pixel = rgb_function(pixel)
            new_im.setPixel(i, j, new_pixel)

    return new_im


def side_by_side(image1, image2, caption):
    """
    Displays two images side-by-side in a window that stays open until you click on it
    :param image1: Image to be displayed on the left
    :param image2: Image to be displayed on the right
    :param caption: String displayed in the frame of the window
    :return:
    """

    width1 = image1.getWidth()
    height1 = image1.getHeight()
    width2 = image2.getWidth()
    height2 = image2.getHeight()

    display = ImageWin(caption, width1 + width2, max(height1, height2))
    image2.setPosition(width1 + 1, 0)
    image1.draw(display)
    image2.draw(display)

    display.exitOnClick()


def chooser(string):
    if string == "negative":
        return negative
    if string == "greyscale":
        return greyscale
    if string == "no red":
        return no_red
    if string == "swirl":
        return swirl
    if string == "no blue":
        return no_blue
    if string == "no green":
        return no_green
    if string == "max red":
        return max_red
    if string == "max green":
        return max_green
    if string == "max blue":
        return max_blue


def main():
    """
    collect command arguments and invoke negative()
    inputs:
        none, fetches arguments using argparse
    effects:
        calls negative()
    """
    parser = argparse.ArgumentParser(description="Displays a transform of the input image")
    parser.add_argument("image", type=str, help="Image to transform")
    args = parser.parse_args()  # gets arguments from command line
    image = args.image
    print("What transformation?")
    print("'negative', 'greyscale', 'no red', 'no green', 'no blue', 'max red', 'max green', 'max blue', or 'swirl'")
    choice = input("")
    rgb_function = chooser(choice)
    transform = transform_image(rgb_function, image)
    old_image = FileImage(image)
    side_by_side(old_image, transform, "Image and Transformed Image")


if __name__ == "__main__":
    main()
