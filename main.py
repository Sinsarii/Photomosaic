# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Load PILLOW

import os, sys
from PIL import Image, ImageEnhance, ImageFilter


def main():
    im = Image.open("base.png")
    # Use a breakpoint in the code line below to debug your script.
    print('Testing Begin')  # Press Ctrl+F8 to toggle the breakpoint.

    # merge_image(im)
    print_image(filter_image(im))


def load_image():
    im = Image.open("base.png")
    # load image into PILLOW
    print('Testing Load Image')


def print_image(image):
    print(image.format, image.size, image.mode)
    image.show()


def enhance_image(image):
    print('Testing enhance image')
    enh = ImageEnhance.Contrast(image)
    enh.enhance(1.3)
    return enh


def filter_image(image):
    image = image.filter(ImageFilter.GaussianBlur)
    return image


def merge_image(image):
    final_image = Image.merge(image.mode, image)
    final_image.show()


if __name__ == '__main__':
    main()
