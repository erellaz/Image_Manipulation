#import sys
import os
from PIL import Image

filepath = "G:\Jpeg"
outpath="G:\cropped"
cropwin=(1000,350,3050,2250)
rot=5.0 #rotation angle clockwise
#______________________________________________________________________________
# Loop through all provided arguments
for filename in os.listdir(filepath):
    if "." not in filename:
        continue
    ending = filename.split(".")[1]
    if ending not in ["jpg", "gif", "png"]:
        continue

    try:
        # Attempt to open an image file
        image = Image.open(os.path.join(filepath, filename))
    except IOError:
        # Report error, and then skip to the next argument
        print("Problem opening", filepath, ":")
        continue

    # Perform operations on the image here
    image = image.crop(cropwin)
    image=image.rotate(rot)

    # Split our origional filename into name and extension 
    name, extension = os.path.splitext(filename)

    # Save the image as "(origional_name)_thumb.jpg
    print(name + '_cropped.jpg')
    image.save(os.path.join(outpath, name + '_cropped.jpg'))

print("-----------All Done-------------")