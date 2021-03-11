import PIL.Image

charcters = ['@', '%', '?', '*', '+', '-', ':', ',', '.']


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

    image_name = input('Enter image name, must same directory as program: ')
    image = PIL.Image.open(image_name)
    file = image_name.split('.')[0]

    new_image = transform(gray(fix_size(image)))

    pixel_count = len(new_image)
    artwork = '\n'.join(new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))


    with open(f'{file}.txt', 'w') as f:
        f.write(artwork)

open_image()