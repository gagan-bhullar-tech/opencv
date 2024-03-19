import cv2
from util import image_show
import numpy as np

# convert from BGR to grayscale
img = cv2.imread("./images/test_image_1.jpg")
img_dim = (img.shape[1], img.shape[0])

# translation
x = 100
y = -100
translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
translated_img = cv2.warpAffine(img, translation_matrix, img_dim)

# rotation
angle = 90
scale = 0.9
print(img_dim)
center = (img_dim[0]/2, img_dim[1]/2)
print(center)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
print(rotation_matrix)
rotated_img = cv2.warpAffine(img, rotation_matrix, img_dim)

image_show(translated_img)
image_show(rotated_img)

cv2.waitKey(0)