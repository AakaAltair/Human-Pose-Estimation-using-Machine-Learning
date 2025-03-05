import cv2

# read image as grayscale
img = cv2.imread(r'E:\aakash\pose detection\playground-image-B3bGG.jpeg', 1)

# get image height, width
(h, w) = img.shape[:2]

# calculate the center of the image
center = (w / 2, h / 2)

angle90 = 90
angle180 = 180
angle270 = 270
scale = 1.0

# Perform the counterclockwise rotation holding at the center
# 90 degrees
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (w, h))

# 180 degrees
M = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Original", img)
cv2.imshow("Rotated by 90 Degrees", rotated90)
cv2.imshow("Rotated by 180 Degrees", rotated180)

cv2.waitKey(0)
cv2.destroyAllWindows()