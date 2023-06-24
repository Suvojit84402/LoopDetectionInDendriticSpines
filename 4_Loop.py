import pyedgeloop as detect
import cv2
import numpy as np
#from PIL import Image

#Loading the image
Im = cv2.imread('skeleton.jpg')

#Invert the image
Im=cv2.bitwise_not(Im)

#Detecting loops
Loops, Edges, Boundary = detect.DetectLoopsEdges(Im)

#print(Loops)
#Convert image
#myimage=np.asarray(Im)
#print(myimage)
#diff_arr=myimage-Loops
#Convert to image
#diff=Image.fromarray(Loops)
#diff.show()
#diff=diff.save("loop.jpg")

#Show the final image
cv2.imshow("Loop",Loops)
cv2.imwrite("loop.jpg",Loops)
cv2.waitKey(0)
