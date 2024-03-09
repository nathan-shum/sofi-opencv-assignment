# import the necessary packages
from pytesseract import Output
import pytesseract
import argparse
import imutils
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="check.jpeg")
args = vars(ap.parse_args())

# load the input image, convert it from BGR to RGB channel ordering,
# and use Tesseract to determine the text orientation
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_osd(rgb, output_type=Output.DICT)

# After getting the rotation angle from Tesseract:
tesseract_angle = results["rotate"]

# If you visually determine you need to rotate 20 degrees more counter-clockwise,
# adjust this value accordingly:
additional_angle = -30  # change this based on your visual inspection

# Calculate the new rotation angle
new_rotation_angle = tesseract_angle - additional_angle  # Adjust based on actual needs

# Now apply this rotation
rotated = imutils.rotate_bound(image, angle=new_rotation_angle)

# display the orientation information
print("[INFO] detected orientation: {}".format(
	results["orientation"]))
print("[INFO] rotate by {} degrees to correct".format(
	results["rotate"]))
print("[INFO] detected script: {}".format(results["script"]))

# Save the rotated image
cv2.imwrite("rotated_check.jpg", rotated)

# show the original image and output image after orientation
# correction
cv2.imshow("Original", image)
cv2.imshow("Output", rotated)
cv2.waitKey(0)