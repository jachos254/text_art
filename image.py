import PIL.Image

charcters = ['#', 'H', 'M', 'X', '@', '%', '?', '*', '+', '-', ':', ',', '.']

def fix_size(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return  resized_image

def gray(image):
    grayscale_image = image.convert('L')
    return grayscale_image

def open_image():

    image_name = input('Enter image name, must same directory as program: ')
    image = PIL.Image.open(image_name)