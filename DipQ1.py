#Uzair Ahmed
#I201751 CS D
#Digital IMmage processing 

import numpy as np
import cv2

# Load the image
image_path = 'E:\data\rect1.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#Check
#To find if Image has been loaded correctly
if image is None:
    print("Error Found Image not Loaded")
    exit(1)

# Find contours in the image
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Check if any contours were found
if not contours:
    print("Sorry no contours were found in the image.")
    exit(1)

#Largest Contour
largest_contour = max(contours, key=cv2.contourArea)

# Rectangle Boundaries
x, y, w, h = cv2.boundingRect(largest_contour)

# Centroid Calculation
centroid_x = x + w // 2

centroid_y = y + h // 2


# Check to see if it is a square or a rectangle
if w == h:
    shape = "Square"

else:
    shape = "Rectangle"

#Showing the Results

print("Detected Shape:", shape)

print("Width:", w)

print("Height:", h)

print("Centroid (x, y):", centroid_x, centroid_y)

# Draw the rectangle on the original image
cv2.rectangle(image, (x, y), (x + w, y + h), 255, 2)

# Display the image with the detected rectangle
cv2.imshow('Detected Object', image)

cv2.waitKey(0)

cv2.destroyAllWindows()
