import cv2 #install it with : conda install -c conda-forge opencv, if DLL error use: pip install opencv-contrib-python
import os

"""
Creates a video from a directory of images
"""

#______________________________________________________________________________
# Input folder with the images and output video name
image_folder = r'G:\R2'
video_name = r'G:\CometNeowise2020-2.avi'

#Frames per seconds
framerate=24
# Codec =-1 for pop up window, o for default
# Popular codecs ae H264, DIVX, MJPEG
codec=cv2.VideoWriter_fourcc(*'DIVX')

#______________________________________________________________________________
# Read the images
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

#Build an OpenCV video object
video = cv2.VideoWriter(video_name, codec, framerate, (width,height))

# Encode the images in the video
for i,image in enumerate(images):
    if i%50 == 0:
        print("Progressed to image",image)
    video.write(cv2.imread(os.path.join(image_folder, image)))

# Release memory
cv2.destroyAllWindows()
video.release()