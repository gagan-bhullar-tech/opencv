import cv2
def image_show(img):
    img = cv2.resize(img, (500, 500))
    cv2.imshow('image', img)
    cv2.waitKey(0)