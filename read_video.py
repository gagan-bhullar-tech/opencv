import cv2

frameWidth = 640
frameHeight = 480

vid = cv2.VideoCapture("videos/test_video.mp4")

while True:
    success, img = vid.read()
    if success:
        img = cv2.resize(img, (frameWidth, frameHeight))
        cv2.imshow("Video", img)
        if cv2.waitKey(71) & 0xFF == ord('q'):
            break