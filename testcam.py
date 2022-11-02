import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = (webcam.read())
    while validacao:
        validacao, frame = (webcam.read())
        cv2.imshow("video", frame)
        key = cv2.waitKey(5)
        if key == 27:
            break

    cv2.imwrite("Eu.png",frame)

    webcam.release()
    cv2.destroyAllWindows()