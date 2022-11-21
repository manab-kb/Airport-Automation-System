import cv2
from simple_facerec import SimpleFacerec
import time

"""
Functions in this file perform the task of image recognition from the live feed of the users device against the saved
images in the image directory of the project. The 'detected' face has a 'red' box surrounding itself from our previous
code. The functions below perform the task of extraction of image metadata from live frames, comparision against stored
metadata of saved images, and display a green box around a face if it is recognised. If not recognized, tries to find
the nearest match.
"""

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("./src/images/")

# Load Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detect Faces
    start = time.time()
    face_locations, face_names = sfr.detect_known_faces(frame)
    print("Overall Time: {}".format(time.time() - start))
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(
            frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2
        )
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
