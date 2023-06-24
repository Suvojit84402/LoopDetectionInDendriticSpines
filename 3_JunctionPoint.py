# import the necessary packages
import numpy as np
import cv2
from opencv_wrapper import * 
# import  poly_point_isect as bot

#Loading the image
image = cv2.imread("skeleton4.11.jpg")
#image=cv2.bitwise_not(image)
# define the list of boundaries
boundaries = [([180, 180, 100], [255, 255, 255])]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

#Detect Junction Points
gray = bgr2gray(output)

corners = cv2.cornerHarris(gray, 9, 3, 0.01)
corners = normalize(corners).astype(np.uint8)

thresh = threshold_otsu(corners)
dilated = dilate(thresh, 3)

contours = find_external_contours(dilated)
image=cv2.bitwise_not(image)
for contour in contours:
    circle(image, contour.center, 3, Color.RED, -1)
    #image[dilated > 0.01 * dilated.max()]=[0, 0, 255]
    #print(contour.center)
    

#Show the final image
cv2.imshow("Image", image)
cv2.imwrite("jp4.jpg",image)
cv2.waitKey(0)