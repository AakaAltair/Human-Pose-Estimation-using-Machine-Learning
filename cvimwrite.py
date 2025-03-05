import cv2
img= cv2.imread(r'E:\aakash\pose detection\playground-image-B3bGG.jpeg',0)
status = cv2.imwrite("abc.png",img)
print("image written:", status)