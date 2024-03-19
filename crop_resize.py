import cv2

img = cv2.imread("images/test_image_1.jpg")
print(img.shape)

# resize image
scale = 0.5
width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)

resize_image = cv2.resize(img, (width, height))
# cv2.imshow("resize image", resize_image)
# cv2.waitKey(0)

# crop image
crop_image = img[100:600, 100:600]
cv2.imshow("crop image", crop_image)
cv2.waitKey(0)