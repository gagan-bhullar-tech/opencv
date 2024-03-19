import cv2
from util import image_show

# convert from BGR to grayscale
img = cv2.imread("./images/test_image_1.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

image_show(rgb)