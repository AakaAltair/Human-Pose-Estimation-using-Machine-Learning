import cv2

# Read image
img = cv2.imread(r'E:\aakash\pose detection\playground-image-B3bGG.jpeg', 1)

# Get height, width, number of channels in the image
dimensions= img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size = img.size

# Print image dimensions
print('Image Dimensions:', img.shape)
print('Image Height:', height)
print('Image Width:', width)
print('Number of Channels:', channels)
print('Image Size:', size)

# Split the image into its BGR channels
b, g, r = cv2.split(img)

# Merge the channels back in BGR order
merged_img_bgr = cv2.merge((b, g, r))

# Merge the channels in RGB order
merged_img_rgb = cv2.merge((r, g, b))

# Display the original image and individual color channels
cv2.imshow('Original Image', img)
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)
cv2.imshow('merged_img_bgr', merged_img_bgr)
cv2.imshow('merged_img_rgb', merged_img_rgb)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
