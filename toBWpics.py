import cv2
import os

path =r"D:\Famille\Richard_resize\\"
dirs = os.listdir( path )

def toBW():
    for item in dirs:
        if os.path.isfile(path+item):
            print("Processing:",item)
            img = cv2.imread(path+item)
            f, e = os.path.splitext(path+item)
            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY,90)
            cv2.imwrite(f + '_BW.jpg', grey)
            
toBW()