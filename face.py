import cv2
import numpy as np

# Load two images
img1 = cv2.imread("C:/Users/ifaiz/OneDrive/Desktop/head.png")
img2 = cv2.imread("C:/Users/ifaiz/OneDrive/Desktop/shirt_pant.png")

# Resize images to same height and width
h, w = 1080, 1080
img1 = cv2.resize(img1, (w, h))
img2 = cv2.resize(img2, (w, h))

# Concatenate images vertically
ver = np.concatenate((img1, img2), axis=0)


# Display result
cv2.imshow('Vertical', ver)
cv2.imwrite('output.png', ver)
cv2.waitKey(0)
