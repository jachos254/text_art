from PIL import Image
import os

mario = Image.open('../mario.jpg')
image = Image.open('../aperture.png')
#img = Image.open(r'C:\Users\Jachos\Desktop\aperture.jpg')
print(mario.size)

def func(x):
   y0 = x + 1
   y1 = x * 3
   y2 = y0 ** 3
   return (y0, y1, y2)

# x = os.listdir()
# print(x)