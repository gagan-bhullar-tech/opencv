import cv2

img = cv2.imread("images/test_image_1.jpg")
print(img)

cv2.imshow("test image", img)
cv2.waitKey()