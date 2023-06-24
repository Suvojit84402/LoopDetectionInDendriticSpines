import cv2
import numpy as np

#Loading the image
image = cv2.imread('skeleton4.11.jpg')

# convert the input image into grayscale color space
operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# modify the data type setting to 32-bit floating point
operatedImage = np.float32(operatedImage)

# apply the cv2.cornerHarris method
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.17)

# Results are marked through the dilated corners
dest = cv2.dilate(dest, None)

image=cv2.bitwise_not(image)
# Reverting back to the original image,with optimal threshold value
image[dest > 0.01 * dest.max()]=[255, 0, 0]

#Show the final image
cv2.imshow('Points', image)
cv2.imwrite("points4.jpg",image)
cv2.waitKey(0)