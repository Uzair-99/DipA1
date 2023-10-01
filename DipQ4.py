import cv2
import numpy as np

def find_area(image, color):
    # Image to BGR
    bgr_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Mask
    #LOwer MAsk
    lower_bound = np.array(color, dtype=np.uint8)
    #Upper Mask
    upper_bound = np.array(color, dtype=np.uint8)
    #Color Mask
    color_mask = cv2.inRange(bgr_image, lower_bound, upper_bound)

    # Calculate the area of the specified color
    area = cv2.countNonZero(color_mask)

    return area

##Main function
def main():
    img_path = 'E:\data\fig1.jpg'
    img = cv2.imread(img_path)

    if img is None:
        print("Error: Unable to load the image.")
        return

    yellow = (102, 217, 254)

    light_gray = (230, 229, 231)
    
    dark_gray = (217, 217, 217)
    
    darkest_gray = (169, 170, 174)

    print("The Area of Yellow:", find_area(img, yellow))
    
    print("The Area of Light Gray:", find_area(img, light_gray))
    
    print("The Area of Dark Gray:", find_area(img, dark_gray))
    
    print("The Area of Darkest Gray:", find_area(img, darkest_gray))

if __name__ == "__main__":
    main()
