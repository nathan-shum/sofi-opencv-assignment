import cv2
import numpy as np

# Load the oriented image
img = cv2.imread('rotated_check.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection or thresholding to find edges
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Check ratio, modify according to your case
RATIO = 3  # This can be changed based on your assumption or ANSI standard

# Initialize variable to store the largest contour that meets the criteria
largest_contour = None
largest_area = 0

# Loop through all contours to find the largest one that meets the width > height * RATIO condition
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    if w > h * RATIO and area > largest_area:
        largest_area = area
        largest_contour = cnt

# Ensure there is a selected contour
if largest_contour is not None:
    x, y, w, h = cv2.boundingRect(largest_contour)
    cropped = img[y:y+h, x:x+w]

    # Show and save the final cropped image
    cv2.imshow('Cropped Check', cropped)
    cv2.imwrite('cropped_check.jpg', cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No suitable contour found.")
