import torch
import numpy as np
import cv2

CONFIDENCE = 0.60
MARGIN = 100

"""
Importing a skeleton custom vision deep learning model from ultralytics to perform the task of face 'detection'.
The model used is a YOLO model - you look only once, which uses R-CNN's to perform the task of image detection by
looking at the network only once and detecting if objects are present.
The model is trained based on weights provided in the pyTorch file, which contains training and testing data and
algorithms suited to best train the model.
Force reload is done to ensure cache is cleared every time the model is run.
"""

model = torch.hub.load(
    "ultralytics/yolov5",
    "custom",
    path="./model/train/exp/weights/last.pt",
    force_reload=True
)

"""
Performing the task of face 'detection' from a live feed of video, by passing frames from the live feed into the
YOLO model and detecting a face if present, and forming a red box around the same if found.
"""

def runFaceDetection(name):
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        results = model(frame)
        getFaces(results, frame, name, cap)

        frameWithFaces = results.render()

        # Dimensions for detector red box
        center = (
            int(frameWithFaces[0].shape[1] / 2),
            int(frameWithFaces[0].shape[0] / 2),
        )

        p1 = (
            center[0] - 100,
            center[1] - 100,
        )

        p2 = (
            center[0] + 100,
            center[1] + 100,
        )

        frameWithRect = cv2.rectangle(
            np.squeeze(frameWithFaces), p1, p2, (0, 255, 0), 2
        )

        # Text to be displayed whilst displaying the red and green boxes for detection and recognition respectively
        frameWithText = cv2.putText(
            frameWithRect,
            "Try to get close to the frame and press S to take a photo.",
            (30, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2,
        )

        frameWithText = cv2.putText(
            frameWithRect,
            "The window will close automatically",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2,
        )

        cv2.imshow("YOLO", frameWithText)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

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

            if cv2.waitKey(10) & 0xFF == ord("s"):
                print("saving image")
                cropped_image = frame[
                    yMin - int(MARGIN * 1.5) : yMin + height + MARGIN,
                    xMin - MARGIN : xMin + width + MARGIN,
                ]
                cv2.imwrite("./public/images/" + name + ".jpg", cropped_image)
                cap.release()
                cv2.destroyAllWindows()


if __name__ == "__main__":
    runFaceDetection()

# python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source 0
