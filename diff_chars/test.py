import PIL.Image
import os
# from chars import asc1, asc2, asc3, asc4, asc5

from chars import *

# random_asc = random_asc()

lista = [asc1, asc2, asc3, asc4, asc5, asc6, random_asc()]

def get_images():
    images = os.listdir('obraski')
    return images

def open_file(image_name):
    image = PIL.Image.open(image_name)
    return image

def fix_size(image, new_width=100):
    width, height = image.size
    ratio = height / width / 2.4
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def gray(resized_image):

    grayscale_image = resized_image.convert('L')
    return grayscale_image


def transform(grayscale_image, choice):
    pixels = grayscale_image.getdata()
    characters = ''.join([choice[pixel // 25] for pixel in pixels])
    return characters

# def number(lista):
#     for i in range(lista)

def create_directories():
    for image in get_images():
        os.makedirs(f'hapsz//{image.split(".")[0]}')



def save_artwork(new_width=100):
    i = 0
    for file in get_images():
        for asc in lista:
            new_image = transform(gray(fix_size(open_file(f'obraski//{file}'))), asc)


            pixel_count = len(new_image)
            artwork = '\n'.join(new_image[i:(i + new_width)] for i in range(0, pixel_count, new_width))
            folder_name = file.split(".")[0]
            file_name = f'{file.split(".")[0]}_{lista.index(asc)}'
            with open(f'hapsz//{folder_name}//{file_name}.txt', 'w', encoding='utf-8') as f:
                f.write(artwork)

            # with open(f'hapsz//{file.split(".")[0]}//{file.split(".")[0]}_{lista.index(asc)}.txt', 'w') as f:
            #     f.write(artwork)
            # i += 1
            # print(artwork)
            # print(i)
