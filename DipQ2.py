import cv2
import numpy as np

#Function to find pixel ratio
def calculate_brown_pixel_ratio(image, color):
    # Image to HSV Convertion
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for brown color in HSV
    lower_bound = np.array([10, 50, 50])  
    
    upper_bound = np.array([30, 255, 255]) 
    
    #Mask for brown color
    brown_mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    
    #Pixel Ratio
    total_pixels = image.shape[0] * image.shape[1]
    
    brown_pixels = cv2.countNonZero(brown_mask)
    
    brown_ratio = brown_pixels / total_pixels
    
    return brown_ratio

#Function to differentiate between genders
def distinguish_gender(img1, img2):
    
    #image 1 brown pixelratio
    brown_ratio_img1 = calculate_brown_pixel_ratio(img1, color)
    
    #image 2 brown pixel ratio
    brown_ratio_img2 = calculate_brown_pixel_ratio(img2, color)

    # Comparision to see if boy or girl
    if brown_ratio_img1 > brown_ratio_img2:
        print("Image 1 is more likely to be of a girl while Image 2 is more likely to be of a boy")
    else:
        print("Image 1 is more likely to be of a boy while Image 2 is more likely to be of a girl")

# Example usage:
img1 = cv2.imread('E:\data\fig3.jpg')

img2 = cv2.imread('E:\data\fig4.jpg')

# Define the brown color in HSV (adjust these values if needed)
color = (10, 50, 50)

distinguish_gender(img1, img2)
