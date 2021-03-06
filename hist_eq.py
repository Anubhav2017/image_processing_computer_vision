import numpy as np 
import cv2
from matplotlib import image as mp_image 
import matplotlib.pyplot as plt 


def improve_contrast(img1):
    
    img=cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    # img=img.ravel()
    # print(img.shape)
    width=img.shape[0]
    height=img.shape[1]

    hist=[0]*256

    for i in range(width):
        for j in range(height):
            hist[img[i][j]]+=1

    #n,_,_=plt.hist(img)
    #hist=list(n)
    #print(hist)

    hist=[el/(height*width) for el in hist]

    mapping=[0]*256
    mapping[0]=hist[0]
    for i in range(1,256):
        mapping[i]=mapping[i-1]+hist[i]

    mapping=[el*255 for el in mapping]

    img2=np.zeros(img.shape)
    for i in range(width):
        for j in range(height):
            img2[i][j]=mapping[img[i][j]]

    hist2=[0]*256

    for i in range(width):
        for j in range(height):
            hist2[int(img2[i][j])]+=1

    hist2=[el/(height*width) for el in hist2]
    
    return img2, hist2,  img,hist

img=cv2.imread("img1.jpeg")
img2,hist2,img1,hist1=improve_contrast(img)

# img=img.ravel()
# plt.hist(img)
# plt.show()

fig=plt.figure()
plt.title("original")
fig.add_subplot(2,1,1)
plt.hist(img1.ravel())
fig.add_subplot(2,1,2)
plt.imshow(img1,cmap='gray')
    

fig=plt.figure()
plt.title("converted")
fig.add_subplot(2,1,1)
plt.hist(img2.ravel())
fig.add_subplot(2,1,2)
plt.imshow(img2,cmap='gray')
plt.show()