import cv2
from detection.simple_facerec import SimpleFacerec
from src.ticket.repository import *
from src.flight.repository import *
from pydispatch import dispatcher

metaKey = "moo"
MyNode = object()

"""
This file contains previously discussed functions to perform the action of both facial detection and recognition; the
only difference being additional attributes have been added into the code, as all these attributes are entries within
the database.
"""

def detectFace():
    ticketStg = TicketStg()
    flightStg = FlightStg()

    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("./public/images")

    # Load Camera
    cap = cv2.VideoCapture(0)
    print("Reading")
    while True:
        ret, frame = cap.read()
        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            ticket = ticketStg.findByName(name)
            if ticket != None:
                flight = flightStg.findById(ticket[3])
                event = {"ticket": ticket, "flight": flight}
                dispatcher.send(metaKey, MyNode, event=event)
            else:
                event = None
                dispatcher.send(metaKey, MyNode, event=event)

            cv2.putText(
                frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2
            )
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            if name == "Unknown":
                cv2.putText(
                    frame,
                    "You cannot proceed",
                    (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2,
                )
            else:
                cv2.putText(
                    frame,
                    "You can proceed",
                    (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

        center = (
            int(frame.shape[1] / 2),
            int(frame.shape[0] / 2),
        )

        p1 = (
            center[0] - 100,
            center[1] - 100,
        )

        p2 = (
            center[0] + 100,
            center[1] + 100,
        )
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)

        cv2.putText(
            frame,
            "Try to get closer to the frame for better detection.",
            (30, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2,
        )

        cv2.putText(
            frame,
            "Press esc to close the window",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2,
        )

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


# detectFace()
