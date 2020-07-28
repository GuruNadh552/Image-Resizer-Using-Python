import PIL
import os
from PIL import Image

x = os.listdir('Guru/')
print('### Image Resizing COde By Guru ###')
j=1
for i in x:
    print()
    y = 'Output/'+i
    img = Image.open('Guru/'+i)
    my_width , my_height = img.size
    img = img.resize((my_width,my_height),PIL.Image.ANTIALIAS)
    img.save(y)
    print('--------> Image ' + str(j) + ' Resized <--------')
    j+=1
print()
print('Image Compression SuccessFully Completed')
print()
    
