import numpy as np 
import cv2
import matplotlib.pyplot as plt
from skimage import morphology as sk_mm
import skimage.color as sk_col
from skimage.filters import try_all_threshold, threshold_minimum, threshold_otsu  


camera = cv2.VideoCapture(0)
size_frame=(128,128)

kernel = sk_mm.selem.square(3)


def record_background(camera):
    while True:
        (grabbed, frame) = camera.read()

        # grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        k=cv2.waitKey(10)
        cv2.imshow("taking background",frame)
        
        if k%27 ==0:
            print("Escape pressed")
            break


        if k%98 ==0:
            print("background taken")
            return frame  
            

    
def inference(camera):

    print("capturing background")

    bg=record_background(camera)

    while True:
        (grabbed, frame) = camera.read()
        # grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        diff = cv2.absdiff(bg.astype("uint8"), frame)
        diff_grey=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        # otsu_val=threshold_minimum(diff_grey)
    
        binary_image=cv2.threshold(diff_grey, 10, 255, cv2.THRESH_BINARY)[1]
        binary_image=sk_mm.opening(binary_image,kernel)
        binary_image=sk_mm.dilation(binary_image,kernel)
        # binary_image=sk_mm.erosion(binary_image)
    
        cv2.imshow("img",binary_image)

        k=cv2.waitKey(10)

        if k%98 ==0:
            print("capturing background")
            bg=record_background(camera) 

        if k%27 ==0:
            print("Escape pressed")
            break
# (grabbed, frame) = camera.read()

# grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# # cv2.imshow("img",grey_frame)
# fig,ax= try_all_threshold(grey_frame)
# plt.show()

inference(camera)