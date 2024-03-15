import cv2

vid = cv2.VideoCapture(0)

frameWidth = 640
frameHeight = 480
vid.set(3, frameWidth)
vid.set(4, frameHeight)

while True:
    ret, frame = vid.read()
    print(ret, frame)
    if ret:
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break