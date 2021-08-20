import cv2
import os

image_folder = r'D:\Dropbox\Jezierski\Edited_scan'
crop_folder = r'D:\Dropbox\Jezierski\Python_crop'

def get_contours(img):
    # First make the image 1-bit and get contours
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(imgray, 120, 255, 0)
    #thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    #cv2.imwrite('thresh.jpg', thresh)
    #img2, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    # filter contours that are too large or small
    size = get_size(img)
    contours = [cc for cc in contours if contourOK(cc, size)]
    return contours

def get_size(img):
    ih, iw = img.shape[:2]
    return iw * ih

def contourOK(cc, size=1000000):
    x, y, w, h = cv2.boundingRect(cc)
    if w < 50 or h < 50: return False # too narrow or wide is bad
    area = cv2.contourArea(cc)
    return area < (size * 0.5) and area > 200

def find_boundaries(img, contours):
    # margin is the minimum distance from the edges of the image, as a fraction
    ih, iw = img.shape[:2]
    minx = iw
    miny = ih
    maxx = 0
    maxy = 0

    for cc in contours:
        x, y, w, h = cv2.boundingRect(cc)
        if x < minx: minx = x
        if y < miny: miny = y
        if x + w > maxx: maxx = x + w
        if y + h > maxy: maxy = y + h

    return (minx, miny, maxx, maxy)

def crop(img, boundaries):
    minx, miny, maxx, maxy = boundaries
    return img[miny:maxy, minx:maxx]

def process_image(fname):
    img = cv2.imread(fname)
    
#    screen_res = 1280, 720
#    scale_width = screen_res[0] / img.shape[1]
#    scale_height = screen_res[1] / img.shape[0]
#    scale = min(scale_width, scale_height)
#    window_width = int(img.shape[1] * scale)
#    window_height = int(img.shape[0] * scale)
#    cv2.namedWindow('Original image', cv2.WINDOW_NORMAL)
#    cv2.resizeWindow('Original image', window_width, window_height)
#    cv2.imshow('Original image',img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    contours = get_contours(img)
    #cv2.drawContours(img, contours, -1, (0,255,0)) # draws contours, good for debugging
    bounds = find_boundaries(img, contours)
    cropped = crop(img, bounds)
#    cv2.imshow('Original image',cropped)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    if get_size(cropped) < 400: return # too small
    cv2.imwrite(os.path.join(crop_folder,os.path.basename(fname)), cropped)


images = [img for img in os.listdir(image_folder) if img.endswith(".JPG")]
for i,image in enumerate(images):
#    if i%10 == 0:
    print("Progressed to image",image)
    process_image(os.path.join(image_folder, image))