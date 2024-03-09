import cv2
import numpy as np

# Load the oriented image
img = cv2.imread('rotated_check.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adjusting the threshold value here
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Or use adaptive threshold

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Modify the RATIO and min_area as needed based on your checks and their sizes
RATIO = 3  # Adjust this based on the actual check size and aspect ratio
min_area = 100  # Adjust this if your check is smaller than expected

'''
# Create a copy of the image to draw contours on for visualization
contour_img = img.copy()
for cnt in contours:
    cv2.drawContours(contour_img, [cnt], -1, (0, 255, 0), 3)
cv2.imshow("All Contours", contour_img)'''


# Loop through all contours to find the largest one that meets the width > height * RATIO condition
largest_contour = None
largest_area = min_area

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    # Temporarily remove or relax the aspect ratio and area constraints to see if the correct contour gets selected
    if area > largest_area:
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
