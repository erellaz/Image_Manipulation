from PIL import Image
Image.MAX_IMAGE_PIXELS=None #for super large image, avoid decompression bomb error
import os

path =r"D:\xxxxxxxx\\"
dirs = os.listdir( path )
factor=0.15
fs=str(int(factor*100))

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            print("Processing:",item)
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((int(im.width * factor), int(im.height * factor)), Image.ANTIALIAS)
            imResize.save(f + ' resized'+fs+'percent.jpg', 'JPEG', quality=90)

resize()
