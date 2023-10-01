import cv2
import numpy as np

def blurimage(image1, image2):
    
    #Image 1 Variance
    var1 = cv2.Laplacian(image1, cv2.CV_64F).var()
   
    #Image 2 Variance
    var2 = cv2.Laplacian(image2, cv2.CV_64F).var()

    #Threshold amount which would check if image is blurred or not
    threshold = 1000

    if var1 < threshold and var2 < threshold:
        print("Both images are blurred.")  #As variance is less than threshold

    elif var1 < threshold:          #As variance of image 1 is less than threshold
        print("Image 1 is blurred while Image 2 is clear.")
        
        cv2.imshow('Clear Image', image2)
        
        cv2.imshow('Blurred Image', image1)

    elif var2 < threshold:      ##As variance of image 2 is less than threshold
        print("Image 1 is clear while Image 2 is blurred.")
        
        cv2.imshow('Clear Image', image1)
        
        cv2.imshow('Blurred Image', image2)
    
    else:       ##Both variance are greater than threshold
        print("Both images are clear.")

    cv2.waitKey(0)

    cv2.destroyAllWindows()

# Loading the images
img1 = cv2.imread('E:\data\fig5.jpg', cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread('E:\data\fig6.jpg', cv2.IMREAD_GRAYSCALE)

# Check to see images were loaded properly
if img1 is None or img2 is None:
    print("Error: Unable to load one or both images.")

else:
    blurimage(img1, img2)
