# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Load PILLOW

import os, sys, numpy, math, PIL
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
from numpy import asarray

IMAGE_LIBRARY_FOLDER = "images/source_library/"
SOURCE_CROPPED_LIBRARY = "images/source_cropped/"
OUTPUT_IMAGE_LIBRARY = "images/output/"


def main():
    prepare_collage_images(200)
    im = Image.open("base.png")
    # Use a breakpoint in the code line below to debug your script.
    # print('Testing Begin')  # Press Ctrl+F8 to toggle the breakpoint.
    im_array = load_image_into_array(im)
    im_width, im_height = im.size
    calculate_block_average_color(im_array, im_width, im_height)
    # test = find_closes_matching_image_to_color([11, 100 , 90], SOURCE_CROPPED_LIBRARY)


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
    # image_array = numpy.asarray(image)
    # image_array = list(image.getdata())
    # im_array = list(image.getdata())
    # return [im_array[i:i + image.width] for i in range(0, len(im_array), image.width)]
    return image_array


def get_image_block(pixel_matrix, corner, block_size):
    opposite_corner = (corner[0] + block_size, corner[1] + block_size)
    block_rows = pixel_matrix[corner[0]:opposite_corner[0]]
    block = []
    for row in block_rows:
        block.append(row[corner[1]:opposite_corner[1]])
    return block


def crop_image(source_image):
    # crop the image
    im_width, im_height = source_image.size
    square_size = min([im_width, im_height])
    crop_box = (0, 0, square_size, square_size)
    region = source_image.crop(crop_box)
    cropped_image = Image.new('RGB', (square_size, square_size), (255, 255, 255, 0))
    cropped_image.paste(region, crop_box)
    return cropped_image


def resize_image(source_image, block_size):
    resized_image = source_image.resize((block_size, block_size))
    return resized_image


def prepare_collage_images(block_size):
    for image in os.listdir(IMAGE_LIBRARY_FOLDER):
        source_image = Image.open(IMAGE_LIBRARY_FOLDER + image)
        cropped_image = crop_image(source_image)
        resize_imaged = resize_image(cropped_image, block_size)
        save_image(resize_imaged, image, SOURCE_CROPPED_LIBRARY)


def save_image(image, image_name, directory):
    image.save(directory + image_name)


def find_closes_matching_image_to_color(block_color, image_directory):
    color_distance = 255
    target_image = ""
    for image in os.listdir(image_directory):
        loaded_image = Image.open(image_directory + image)
        cropped_image_array = load_image_into_array(loaded_image)
        average_color_cropped = find_average_color(cropped_image_array)
        compared_color_distance = find_color_distance(block_color, average_color_cropped)
        if compared_color_distance < color_distance:
            color_distance = compared_color_distance
            target_image = image
    return target_image


def find_color_distance(color_base, color_cropped):
    distance = math.sqrt(((color_base[0] - color_cropped[0]) ** 2) + ((color_base[1] - color_cropped[1]) ** 2) + (
            (color_base[2] - color_cropped[2]) ** 2))
    return distance


def find_average_color(image_array):
    r_total = 0
    g_total = 0
    b_total = 0
    pixel_number_total = 0
    # for x in range(0, len(image_array) - 1):
    #    for y in range(0, len(image_array) - 1):
    #        red_list.append(image_array[x][y][0])
    #        green_list.append(image_array[x][y][1])
    #        blue_list.append(image_array[x][y][2])
    for row in image_array:
        for color_tuple in row:
            r_total += color_tuple[0]
            g_total += color_tuple[1]
            b_total += color_tuple[2]
            pixel_number_total += 1

    # r = int(round(sum(red_list) / len(red_list)))
    # g = int(round(sum(green_list) / len(green_list)))
    # b = int(round(sum(blue_list) / len(blue_list)))
    r_average = int(round(r_total / pixel_number_total))
    g_average = int(round(g_total / pixel_number_total))
    b_average = int(round(b_total / pixel_number_total))

    # print(r)
    # print(g)
    # print(b)

    # return r, g, b
    return r_average, g_average, b_average


def color_block(color, new_image, x, y, block_width, block_height):
    draw = ImageDraw.Draw(new_image)
    draw.rectangle((x, y, block_width, block_height), fill=(color[0], color[1], color[2]))


def calculate_block_average_color(image_array, image_width, image_height):
    # for the size of the image, iterate and grab every tuple into two dimensional array
    output_image = Image.new('RGB', (image_width, image_height), (255, 255, 255, 0))
    block_array = []
    block_width = 200
    block_height = 200
    total = 0
    # divide by floor length to put into array and add them all
    draw = ImageDraw.Draw(output_image)

    for row in range(0, image_width - 1, block_width):
        # divide by floor height to put into right array to add them all
        for col in range(0, image_height - 1, block_height):
            # print("Row #" + str(row))
            # print("Col #" + str(col))
            block = get_image_block(image_array, (col, row), block_width)
            # block = get_image_square(image_array, (row, col), block_width)
            average_color = find_average_color(block)
            # average_color = mean_rgb(block)
            # draw needs to be x0,y0, x0+width, y0+ height

            matching_image = find_closes_matching_image_to_color(average_color, SOURCE_CROPPED_LIBRARY)
            block_image = Image.open(SOURCE_CROPPED_LIBRARY + matching_image)
            output_image.paste(block_image, (row, col))
            # draw.rectangle((row, col, row + block_width, col + block_height), fill=(average_color[0], average_color[1], average_color[2]))
            output_image.show()
        # print(image_array[row][col])

        # add the amount to total

    # for the amount of blocks in the image, calculate the average R,G,B of the block size
    output_image.show()


if __name__ == '__main__':
    main()
