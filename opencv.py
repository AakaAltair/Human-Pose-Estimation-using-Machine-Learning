import cv2
import numpy as np

# Create a numpy array filled with zeros to use as a blank image
image = np.zeros((512, 512, 3), np.uint8)

# Draw a green line on the image
cv2.line(image, (0, 0), (511, 511), (0, 255, 0), 5)

# Draw a red rectangle on the image
cv2.rectangle(image, (384, 0), (510, 128), (0, 0, 255), 3)

# Draw a blue circle on the image
cv2.circle(image, (447, 63), 63, (255, 0, 0), -1)

# Display the image
cv2.imshow('Image', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
