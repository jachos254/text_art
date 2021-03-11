import PIL.Image
import os
# from chars import asc1, asc2, asc3, asc4, asc5

from chars import *

choice = random_asc()

def ask_user():
    while True:
        image_name = 'db.png'
        #image_name = input('Enter image name, must be in the same directory as program: ')
        if image_name in os.listdir():
            break


    return image_name

def get_images():
    images = os.listdir(obraski)
    return images

def open_file():
    image_name = ask_user()
    file = image_name.split('.')[0]
    image = PIL.Image.open(image_name)
    return image, file

def fix_size(new_width=100):
    image = open_file()
    file = image[1]
    width, height = image[0].size
    ratio = height / width / 2.4
    new_height = int(new_width * ratio)
    resized_image = image[0].resize((new_width, new_height))
    return resized_image, file


def gray():
    resized_image = fix_size()
    file = resized_image[1]
    grayscale_image = resized_image[0].convert('L')
    return grayscale_image, file


def transform():
    grayscale_image = gray()
    file = grayscale_image[1]
    pixels = grayscale_image[0].getdata()
    characters = ''.join([choice[pixel // 25] for pixel in pixels])
    return characters, file


def save_artwork(new_width=100):


    new_image = transform()
    file = new_image[1]
    final_image = new_image[0]
    pixel_count = len(final_image)
    artwork = '\n'.join(final_image[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    # with open(f'{file}.txt', 'w') as f:
    #     f.write(artwork)

    print(artwork)
