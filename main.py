# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Load PILLOW

import os, sys, numpy
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw


def main():
    im = Image.open("base.png", 'r')
    # Use a breakpoint in the code line below to debug your script.
    print('Testing Begin')  # Press Ctrl+F8 to toggle the breakpoint.

    # merge_image(im)
    im_array = load_image_into_array(im)
    # calculate_block_average_color(im_array, im.height, im.width)
    convert_matrix_into_strip(im_array, 0, 0, 50, 50)


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


def shrink_image_by_half(image):
    with image as im:
        (width, height) = (im.width // 2, im.height // 2)
        im_resized = im.resize((width, height))
    return im_resized


def rotate_image_upside_down(image):
    theta = 180
    im_rotated = image.rotate(angle=theta)
    return im_rotated


def load_image_into_array(image):
    # load image into array
    image_array = numpy.array(image)
    # image_array = list(image.getdata())
    return image_array


def find_average_color(image_array, corner_x, corner_y, block_width, block_height):
    red_list = []
    green_list = []
    blue_list = []
    for x in range(corner_x, corner_x + block_width):
        for y in range(corner_y, corner_y + block_height):
            red_list.append(image_array[x][y][0])
            green_list.append(image_array[x][y][1])
            blue_list.append(image_array[x][y][2])
    r = sum(red_list) / len(red_list)
    g = sum(green_list) / len(green_list)
    b = sum(blue_list) / len(blue_list)

    print(r)
    print(g)
    print(b)


def calculate_block_average_color(image_array, image_height, image_width):
    # for the size of the image, iterate and grab every tuple into two dimensional array
    block_array = []
    block_width = 50
    block_height = 50
    total = 0
    # divide by floor length to put into array and add them all
    for row in range(0, image_width - 1, block_height):
        # divide by floor height to put into right array to add them all
        for col in range(0, image_height - 1, block_width):
            print(image_array[row][col])

            # add the amount to total

    # for the amount of blocks in the image, calculate the average R,G,B of the block size


if __name__ == '__main__':
    main()
