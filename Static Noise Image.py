#trial 1???
#  import random
# import matplot


# random.random()

# plt.imshow()




#trial 2??
import PIL, random
import matplotlib.pyplot as plt 
import os.path  
import PIL.ImageDraw            
from PIL import Image, ImageDraw, ImageFilter


im = Image.new("RGB", (300,300))

for r in range(0,300):
    for c in range(0,300):
        re = random.randint(0, 255)
        gr = random.randint(0, 255)
        bl = random.randint(0, 255)
        im[r][c]=[re,gr,bl]
im.show()

bl = random.randint(0, 255)
im[r][c]=[re,gr,bl]
im.show()




#trial 3?
import numpy as np
from random import randint
from PIL import Image

array = np.array([[[randint(0, 255),randint(0, 255),randint(0, 255)]] for i in range(100)])
array =  np.reshape(array.astype('uint8'), (10, 10, 3))
img = Image.fromarray(np.uint8(array.astype('uint8')))

img.save('pil_color.png')







#trial 4?
import numpy as np
from PIL import Image

arr = np.random.randint(low = 0, high = 255, size = (300, 300, 3))

im = Image.fromarray(arr.astype('uint8'))
im.show()



#trial 5??
array1 = []
for x in range(y):
