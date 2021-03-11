

import PIL.Image

charcters = ['_', '░', '8', '░', '*', '_', '¶', '_', '_']

def fix_size(image, new_width=100):
    width, height = image.size
    ratio = height / width / 2.6
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return  resized_image

def gray(image):
    grayscale_image = image.convert('L')
    return grayscale_image

def transform(image):
    pixels = image.getdata()
    characters = ''.join([charcters[pixel // 25] for pixel in pixels])
    return characters

def open_image(new_width=100):

    #image_name = input('Enter image name, must same directory as program: ')
    file = 'alejak.jpg'
    name = file.split('.')[0]

    image = PIL.Image.open(file)

    new_image = transform(gray(fix_size(image)))

    pixel_count = len(new_image)
    artwork = '\n'.join(new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    print(artwork)

    with open(f'{name}.txt', 'w', encoding='utf-8') as f:
        f.write(artwork)

open_image()