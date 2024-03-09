import cv2 as cv
img = cv.imread("dog-side-eye.jpeg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a k