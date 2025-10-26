#Description: this is a program that can operate the below functions on a image in ppm format

#(a) Functionnegative(image_list)
#This function returns a 2D array containing the new image pixels. A negative image contains pixels 
#in which the red, green and blue values have been subtracted from 255. 
#If a pixel value is [255, 34, 100] then the negative pixel will be: [0, 221, 155]. 

#(b) Functionrotate_left_90(image_list)
#In this function you will, as the function name suggests, rotate the image image_list by 90 degrees, 
#rotating it to the left. The source image may have a different width and height as shown in the example below. 

#(c) Functioncrop(image_list,crop_X,crop_Y,crop_width,crop_height)
#This function returns a 2D array containing the image pixels. 
#Cropping an image involves reducing the size of the image so that the top-left pixel of new image is the pixel 
#in the old image with coordinates crop_X and crop_Y. The crop_width and the crop_height are the width and height
#of the new image in pixels.

#(d) Functionblur(image_list)
#In this function you will take an image and implement a blur filter. 
#The algorithm to do this creates a new image in which a pixel’s values are averaged with the values of the 
#immediate neighbours. 
#Pixels at the edge of the image need to be treated slightly differently. In this example, consider the pixel 
#at (1,0). The average has fewer data points and the new pixel generated for the position (1,0) will be:
#red value: (0 + 100 + 0 + 0 + 0 + 0) / 6 = 16 green value: (0 + 0 + 0 + 0 + 255 + 0) / 6 = 42 
#bluevalue:(0+0+0+0+175+0) / 6=29 pixel value is [16, 42, 29]

import os

HEADER = 3
OPTION_RANGE = 4
RED = 0
GREEN = 1
BLUE = 2


def negative(image_list):
    """Create a negative of the image

    Args:
        image_list (list): 2D list containging an image

    Returns:
        list: 2D list containing a negative image
    """
    pass


def crop(image_list, crop_X, crop_Y, crop_width, crop_height):
    """Crop image with origin crop_X, crop_Y and given width and height.

    Args:
        image_list (list): the image
        crop_X (int): X coordinate, counting from 0, of the 
                      top-left pixel of the cropped region.
        crop_Y (int): Y coordinate, counting from 0, of the 
                      top-left pixel of the cropped region.
        crop_width (int): width of cropped region in pixels.
        crop_height (int): height of cropped region in pixels.

    Returns:
        list : 2D list containing cropped image
    """
    pass


def rotate_left_90(image_list):
    """Rotate an image 90 degrees left

    Args:
        image_list (list): image to rotate.

    Returns:
        list : rotated image
    """
    pass


def blur(image_list):
    """Blur an image

    Args:
        image_list (list): 2D list containing the image pixels.

    Returns:
        list: 2D list containing the blurred image pixels.
    """
    pass



def get_valid_filename(prompt):
    """Use prompt (a string) to ask the user to type the name of a file. If
	the file does not exist, keep asking until they give a valid filename.

        Args:
        prompt (str): prompt for the user

    Returns:
        str : name of the file
    """
    filename = input(prompt)
    while not os.path.exists(filename):
        print("That file does not exist.")
        filename = input(prompt)
    return filename


def print_menu():
    """Print the menu for the application
    """
    print("\n\n\toptions: ")
    print("\t\t[1]  negative")
    print("\t\t[2]  rotate left 90")
    print("\t\t[3]  crop")
    print("\t\t[4]  blur")


def get_menu_option(prompt):
    """Get the menu option from the user and return the option.

    Args:
        prompt (str): text for prompt

    Raises:
        ValueError: Use exception to trap cases where the user has not entered
                    a valid number

    Returns:
        int : option number
    """
    valid_option = False

    while not valid_option:
        print_menu()
        try:
            option = int(input(prompt))
            if option in range(1, OPTION_RANGE + 1):
                valid_option = True
            else:
                raise ValueError
        except ValueError:
            print("\n\n\tthat's not a valid choice, please try again.")
    return option


def read_image(filename):
    """Read a PPM image from filename

    Args:
        filename (str): name of file

    Returns:
        list: 2D list containing the image
    """
    file = open(filename, 'r')

    # Ignore the first line, we don't need it
    file.readline()
    dimensions = file.readline().split()
    columns, rows = int(dimensions[0]), int(dimensions[1])

    # Ignore the third line, assume colour depth is 255
    file.readline()

    # Read the remaining lines into a list
    file_contents = file.readlines()

    # merge the lines of the list into a single 1D list
    # convert the strings to integers.
    all_numbers = []
    for line in file_contents:
        all_numbers += [int(j) for j in line.rstrip().split()]
   
    # Transform the file contents into a 2D list with the dimensions of the image

    image = []
    offset = 0

    for row in range(rows):
        image.append([])
        for col in range(columns):
            rgb = all_numbers[offset : offset + 3]
            image[row].append(rgb)
            offset += 3

    return image


def write_image(image, filename):
    """Write a 2D list representing the image to the filename

    Args:
        image (list): 2D list containing image
        filename (str): name of file to write
    """

    rows = len(image)
    cols = len(image[0])

    file = open(filename, 'w')
    file.write("P3\n{0:d} {1:d}\n255\n".format(cols, rows))

    for row in range(rows):
        for col in range(cols):
            rgb = image[row][col]
            file.write("{} {} {}  ".format(rgb[RED], rgb[GREEN], rgb[BLUE]))
        file.write("\n")


def get_dimensions():
    """Get the dimensions of the crop region

    Returns:
        tuple: contains the X,Y origin of the cropped region and the width
                and height of the crop region.
    """
    dimensions_string = input(
        "\t\tEnter the origin x,y and the width and height separated by commas: ")\
            .split(',')
    return int(dimensions_string[0]), int(dimensions_string[1]),\
             int(dimensions_string[2]), int(dimensions_string[3])


def main():
    print("Welcome to the Portable Pixmap (PPM) Image Editor!")

    prompt = "\n\tenter the name of the image file: "
    filename = get_valid_filename(prompt)

    image_list = read_image(filename)

    output_image_filename = input("\n\tenter the name of the output file: ")

    prompt = "\n\tyour choice: "
    menu_choice = get_menu_option(prompt)

    if menu_choice == 1:
        new_image = negative(image_list)
    elif menu_choice == 2:
        new_image = rotate_left_90(image_list)
    elif menu_choice == 3:
        crop_X, crop_Y, width, height = get_dimensions()
        new_image = crop(image_list, crop_X, crop_Y, width, height)
    elif menu_choice == 4:
        new_image = blur(image_list)
    
    write_image(new_image, output_image_filename)
    
    print("\nImage written to file", output_image_filename)


if __name__ == '__main__':

    main()
