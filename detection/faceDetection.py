import numpy as np
import cv2

CONFIDENCE = 0.60
MARGIN = 100

"""
Helper function for face detection. This function uses the array of results returned by the YOLO model, 
enumerates them into a key value pair object, and matches the returned attributes against a level of confidence to 
detect if the face found in the feed holds true. If so, calculates the height and width of the image as best suited
for the 'recognition' model, and then saves the image into a project directory when prompted by the user to do so.
"""

def getFaces(results, frame, name, cap):
    faces = []
    for i, dets in enumerate(results.xyxy[0]):
        if dets[4] > CONFIDENCE and dets[5] == 0:
            xMin = int(dets[0].numpy())
            yMin = int(dets[1].numpy())
            xMax = int(dets[2].numpy())
            yMax = int(dets[3].numpy())

            height = yMax - yMin
            width = xMax - xMin
            # print(height)
            # print(width)
            if cv2.waitKey(10) & 0xFF == ord("s"):
                print("Saving Image")
                cropped_image = frame[
                    yMin - int(MARGIN * 1.5) : yMin + height + MARGIN,
                    xMin - MARGIN : xMin + width + MARGIN,
                ]
                cv2.imwrite("./public/images/" + name + ".jpg", cropped_image)
                cap.release()
                cv2.destroyAllWindows()
