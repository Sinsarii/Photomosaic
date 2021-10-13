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
    #image_array = numpy.array(image)
    # image_array = list(image.getdata())
    im_array = list(image.getdata())
    return [im_array[i:i + image.width] for i in range(0, len(im_array), image.width)]
    # return image_array


def get_image_block(pixel_matrix, corner, block_size):
    opposite_corner = (corner[0] + block_size, corner[1] + block_size)
    block_rows = pixel_matrix[corner[0]:opposite_corner[0]]
    block = []
    for row in block_rows:
        block.append(row[corner[1]:opposite_corner[1]])
    return block


def process_image_block(source_image, x, y, block_width, block_height, r, g, b):
    box = (x, y, block_width, block_height)
    region = source_image.crop(box)
    region = region.fill()
    avg_color_block = Image.new(mode="RGB", size=(block_width, block_height), color=(r, g, b))


def mean_rgb(pixels):
    """Calculates the mean RGB value of the given pixel
    matrix.
    Args:
    pixels -- a 2-D pixel matrix
    Returns:
    A 3-tuple of the average RGB value of the matrix
    """
    r_total = 0
    g_total = 0
    b_total = 0
    n_pixels = 0
    for row in pixels:
        for p in row:
            r_total += p[0]
            g_total += p[1]
            b_total += p[2]

            n_pixels += 1

    return int(round(r_total / n_pixels)), int(round(g_total / n_pixels)), int(round(b_total / n_pixels))


def get_image_square(pixels, corner, size):
    """Returns a square sub-section of the `pixels` matrix,
    with top-left corner at `corner`, and each side of the
    square `size` pixels in length.
    Args:
    pixels -- the pixels matrix of the entire image
    corner -- the top-left corner of the sub-section
    size -- the size of each side of the sub-section
    Returns:
    A pixel matrix of a sub-section of the original matrix
    """
    opposite_corner = (corner[0]+size, corner[1]+size)

    square_rows = pixels[corner[0]:opposite_corner[0]]
    square = []
    for row in square_rows:
        square.append(row[corner[1]:opposite_corner[1]])

    return square


def find_average_color(image_array):
    red_list = []
    green_list = []
    blue_list = []
    for x in range(0, len(image_array) - 1):
        for y in range(0, len(image_array) - 1):
            red_list.append(image_array[x][y][0])
            green_list.append(image_array[x][y][1])
            blue_list.append(image_array[x][y][2])
    r = int(round(sum(red_list) / len(red_list)))
    g = int(round(sum(green_list) / len(green_list)))
    b = int(round(sum(blue_list) / len(blue_list)))

    print(r)
    print(g)
    print(b)

    return r, g, b


def color_block(color, new_image, x, y, block_width, block_height):
    draw = ImageDraw.Draw(new_image)
    draw.rectangle((x, y, block_width, block_height), fill=(color[0], color[1], color[2]))


def calculate_block_average_color(image_array, image_width, image_height):
    # for the size of the image, iterate and grab every tuple into two dimensional array
    output_image = Image.new('RGB', (image_width, image_height), (255, 255, 255, 0))
    block_array = []
    block_width = 100
    block_height = 100
    total = 0
    # divide by floor length to put into array and add them all
    draw = ImageDraw.Draw(output_image)

    for row in range(0, image_width - 1, block_width):
        # divide by floor height to put into right array to add them all
        for col in range(0, image_height - 1, block_height):
            # print("Row #" + str(row))
            # print("Col #" + str(col))
            block = get_image_block(image_array, (row, col), block_width)
            # block = get_image_square(image_array, (row, col), block_width)
            average_color = find_average_color(block)
            # average_color = mean_rgb(block)
            #draw needs to be x0,y0, x0+width, y0+ height
            draw.rectangle((row, col, row + block_width, col + block_height),
                           fill=(average_color[0], average_color[1], average_color[2]))
            # output_image.show()
        # print(image_array[row][col])

        # add the amount to total

    # for the amount of blocks in the image, calculate the average R,G,B of the block size
    output_image.show()


if __name__ == '__main__':
    main()
