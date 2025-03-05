#importing the opencv module
import cv2
# using imread('path') and 0 denotes read as grayscale image img = cv2.imread(r'Gan.jpeg',1)
# Path to the image
image_path = r'E:\aakash\pose detection\playground-image-B3bGG.jpeg'

# Reading the image in color mode (1 denotes color)
img = cv2.imread(image_path, 1)
cv2.imshow('Image', img)
#img= cv2.imread(r'E:\aakash\pose detection',1)

print (img)
img1=cv2.cvtColor (img, cv2.COLOR_BGR2GRAY) 
img2=cv2.cvtColor (img, cv2.COLOR_BGR2RGB) 
img3=cv2.cvtColor (img, cv2.COLOR_BGR2HSV) 
img4=cv2.cvtColor (img, cv2.COLOR_BGR2LAB) 
#This is using for display the image cv2.imshow('color_image', img)

cv2.imshow('Gray_image', img1)
cv2.imshow('RGB_image', img2)
cv2.imshow('HSV_image', img3)
cv2.imshow('LAB_image', img4)
cv2.waitKey(0) # This is necessary to be required so that the image doesn't #It will run continuously until the key press.
cv2.destroyAllWindows()

