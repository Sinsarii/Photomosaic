# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Load PILLOW

import os, sys, numpy
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw


def main():
    im = Image.open("base.png")
    # Use a breakpoint in the code line below to debug your script.
    print('Testing Begin')  # Press Ctrl+F8 to toggle the breakpoint.

    # merge_image(im)
    im_array = load_image_into_array(im)
    im_width, im_height = im.size
    calculate_block_average_color(im_array, im_width, im_height)


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


def get_image_block(pixel_matrix, corner_x, corner_y, block_size):
    opposite_corner = (corner_x + block_size, corner_y + block_size)
    block_rows = pixel_matrix[corner_x:opposite_corner[0]]
    block = []
    for row in block_rows:
        block.append(row[corner_y:opposite_corner[1]])
    return block


def process_image_block(source_image, x, y, block_width, block_height, r, g, b):
    box = (x, y, block_width, block_height)
    region = source_image.crop(box)
    region = region.color
    avg_color_block = Image.new(mode="RGB", size=(block_width, block_height), color=(r, g, b))


def find_average_color(image_array):
    red_list = []
    green_list = []
    blue_list = []
    for x in range(0, len(image_array) - 1):
        for y in range(0, len(image_array) - 1):
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
            if row <= image_width & col <= image_height:
                block = get_image_block(image_array, row, col, block_width)
                find_average_color(block)
            # print(image_array[row][col])

            # add the amount to total

    # for the amount of blocks in the image, calculate the average R,G,B of the block size


if __name__ == '__main__':
    main()
