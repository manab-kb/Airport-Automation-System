import face_recognition
import cv2
import os
import glob
import numpy as np
import time

"""
GUI class for performing face 'recognition'. Produces and reads image metadata, compares with previously saved metadata. 
Mimics a recognition model, Checks for perfect/nearest/best matches of metadata and appends names to the list 
of known names, if a good match is found.
"""

class SimpleFacerec:
    # Constructor to initialize private variables

    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed 0.25
        self.frame_resizing = 0.25

    """
    Function to read all images present in the image directory of the project, store information about their encoding
    in a the above declared encoding list, and store their filenames in the also above declared names list. This will
    be further used by the face 'recognition' model, as image metadata.
    """

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    """
    Performs the task of face recognition on 'known' images by simulating a model. The below function captures live feed 
    from the 'detected' face in frames, calculates the image metadata (image name and encoding) of each frame, checks if
    the metadata of any frame captured matches the metadata of the saved images exactly. If yes, proceeds with
    appending name to the list. If not, checks for the nearest match (uses KNN) to the metadata among all saved images. 
    If finds a good match with a good level of accuracy, then proceeds with appending name to the list of known names. 
    """

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        start = time.time()
        face_locations = face_recognition.face_locations(rgb_small_frame, model="hog")
        print(face_locations)
        print("Weather Location: {}".format(time.time() - start))

        start = time.time()
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        print("Face Time: {}".format(time.time() - start))

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            start = time.time()
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            print("Compared Time: {}".format(time.time() - start))
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
