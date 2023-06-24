import cv2
from numpy import asarray
import numpy as np
from skimage.morphology import skeletonize

#Loading the image
file = "Original_image.tif"
img_grey = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
afterMedian = cv2.medianBlur(img_grey, 3)
thresh = 140

# threshold the image
img_binary = cv2.threshold(afterMedian, thresh, 255, cv2.THRESH_BINARY)[1]

# make binary image
arr = asarray(img_binary)
binaryArr = np.zeros(asarray(img_binary).shape)
for i in range(0, arr.shape[0]):
    for j in range(0, arr.shape[1]):
        if arr[i][j] == 255:
            binaryArr[i][j] = 1
        else:
            binaryArr[i][j] = 0


cv2.imshow("Binary", binaryArr)

# perform skeletonization
backgroundSkeleton = skeletonize(binaryArr)

# convert to non-binary image
bSkeleton = np.zeros(arr.shape)
for i in range(0, arr.shape[0]):
    for j in range(0, arr.shape[1]):
        if backgroundSkeleton[i][j] == 0:
            bSkeleton[i][j] = 0
        else:
            bSkeleton[i][j] = 255

#Show the final images
cv2.imshow("Skeleton", bSkeleton)
cv2.imwrite("skeleton1.jpg",bSkeleton)
cv2.waitKey(0)