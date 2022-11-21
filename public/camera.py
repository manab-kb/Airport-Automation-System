import cv2

"""
User defined modular code to capture and pass frames of images from a live video feed, provided by the devices' camera.
The feed stops when prompted by clicking on the key mentioned - based on how pyQt5 works, one cannot close a window 
of live feed directly by clicking the close button from the GUI.
"""

capture = cv2.VideoCapture(0)

while (capture.isOpened()):
    ret, frame = capture.read()
    print(frame)
    cv2.imshow('webCam',frame)
    if (cv2.waitKey(1) == ord('s')):
        break

capture.release()
cv2.destroyAllWindows()