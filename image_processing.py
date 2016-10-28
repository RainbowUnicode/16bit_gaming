"""
Let's start working on image processing skills.
"""

from cImage import *

cat_window = ImageWin("Cat image", 500, 500)
cat_image = FileImage("cat.gif")
cat_image.draw(cat_window)
cat_window.exitOnClick()