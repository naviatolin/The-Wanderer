"""
Contains all the classes used for computer vision and backend processing.

@author: Duncan Mazza
Stripped down for Raspi by Michael Remley
@revision: v1.4
"""
# pip install opencv-python
# pip install opencv-contrib-python
import cv2
from math import acos, cos, sin
import numpy as np
import os


class ProcessingEngine:
    """
    The backend class for image per-processing.
    """

    def __init__(self, threshold=30, debug=False):
        # load the COCO class labels our YOLO model was trained on
        cwd = os.getcwd()
        self.DETECTION_THRESHOLD = 0.4  # minimum confidence level for person to be recognized
        print(cwd)

        labelsPath = "/home/pi/The-Wanderer/Firmware/yolo-coco/coco.names"

        self.weightsPath = "/home/pi/The-Wanderer/Firmware/yolo-coco/yolov3.weights"
        self.configPath = "/home/pi/The-Wanderer/Firmware/yolo-coco/yolov3.cfg"
        self.LABELS = open(labelsPath).read().strip().split("\n")

        self.ln = 0  # a placeholder (for determining only the *output* layer names that we need from YOLO)
        # that is overridden when self.turn_on() is called

        self.n = 0  # counter for the calibration process
        self.threshold = threshold  # minimum number of frames used to perform calibration

        self.debug = debug

        self.cap_dict = {}  # store the OpenCV captures in a dictionary
        self.detect_dict = {}  # store detected outputs in a dictionary

        self.sees_person = False

        # How closely to look at the image, 1:(320,320) looks closer than 2:(128,128)
        self.reading_frames = {1: (320, 320), 2: (128, 128), 3: (96, 96), 4:(32,32)}

    def turn_on(self):
        """
        This method loads all of the OpenCV camera captures into self.cap_dict and, and also loads all of the
        objects used for detection and stores them in self.detect_dict. One of the main purposes of this function is
        so that the camera(s) is/are not turned on until the select_feeds.html file is opened.
        :param filename: path to the video file being uploaded if not using the live camera footage
        :return:
        """
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            # Representation of dictionary entries: [OpenCV capture, calibration boolean, 0 which is a placeholder
            # for the calibration matrix, 1, which is boolean for whether the camera is to be used, and (height,
            # width) of the camera frame]
            self.cap_dict = [cap, 0, 0, 1, (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                                               int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))]
            print("[INFO] loading YOLO from disk for camera {}...".format(0))
            self.detect_dict = cv2.dnn.readNetFromDarknet(self.configPath,
                                                             self.weightsPath)  # load our YOLO object detector trained on COCO dataset (80 classes)
            print("[INFO] finished loading YOLO for camera {}...".format(0))
            # the following part only needs to be initialized once, but it is in this for loop because
            #  the at least one cv2.dnn.readNetFromDarknet(...) has to have been initialized for this part to
            # be initialized.

            # determine only the *output* layer names that we need from YOLO
            self.ln = self.detect_dict.getLayerNames()
            self.ln = [self.ln[i[0] - 1] for i in self.detect_dict.getUnconnectedOutLayers()]

    def turn_off(self):
        """
        Releases the OpenCV device and clears the appropriate attributes from the class.
        :return: void
        """

        self.cap_dict.release()
        self.cap_dict = {}

    def _parse_detected(self, frame, layerOutputs):
        """
        This function takes the output of the object detection and parses the information down to bounding box
        coordinates of any people that the algorithm detects.

        This method was derived from the example at this link:
        https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/
        credit to: Adrian Rosebrock

        :param frame: input frame to the object detection
        :param w: width of the frame
        :param h: height of the frame
        :param layerOutputs: output from the object detection
        :param LABELS: labels for the YOLO model
        :return: boxes, frame_copy: bounding boxes for the detected people, a copy of the frame with bounding boxes
        drawn
        """
        boxes = []
        confidences = []
        classIDs = []

        # frame width and height
        W = self.cap_dict[4][1]
        H = self.cap_dict[4][0]

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability) of the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)

                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected probability is greater than the minimum
                # probability
                if confidence > self.DETECTION_THRESHOLD:
                    # scale the bounding box coordinates back relative to the size of the image, keeping in mind that
                    # YOLO actually returns the center (x, y)-coordinates of the bounding box followed by the boxes'
                    # width and height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    # use the center (x, y)-coordinates to derive the top and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates, confidences, and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        # apply non-maxima suppression to suppress weak, overlapping bounding boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.DETECTION_THRESHOLD, 0.3)

        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                if self.LABELS[classIDs[i]] != 'person':
                    frame_copy = frame
                    return [], frame_copy
                else:
                    self.sees_person = True
                    # extract the bounding box coordinates
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])

                    # modify boxes such that it includes the top left and bottom right coordinates as opposed to the top
                    # left coordinates and the length and width of the box
                    boxes[i][2] = x + w
                    boxes[i][3] = y + h

                    # draw a bounding box rectangle and label on the image
                    color = (157, 161, 100)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    text = "{}: {:.4f}".format(self.LABELS[classIDs[i]], confidences[i])
                    cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        else:
            self.sees_person = False
        frame_copy = frame
        return boxes, frame_copy

    def get_frame(self):
        """
        Returns the captured frame that is warped by the calibration_matrix
        :return: frame or frame converted to bytes, depending on use case
        """
        # if the camera is set to off, then dim the frame by x0.2

        cap = self.cap_dict[0]  # select the camera from self.cap_dict
        _, frame = cap.read()  # read the camera capture

        # pull out the height and width of the camera frame
        height = self.cap_dict[4][0]
        width = self.cap_dict[4][1]

        net = self.detect_dict  # select the image processor (net)
        blob = cv2.dnn.blobFromImage(frame,
                                        1 / 255.0,
                                        (64,64), # Reading frame, smaller values run faster
                                        swapRB=True,
                                        crop=False)  # pre=process the image for detection

        # run detection on the frame:
        net.setInput(blob)
        layerOutputs = net.forward(self.ln)
        boxes, frame = self._parse_detected(frame, layerOutputs)

        return frame if self.debug else cv2.imencode('.jpg', frame)[1].tobytes()

    def person_detected(self):
        # Run detection on a frame
        frame = self.get_frame()
        # Return if a person was seen
        return self.sees_person


if __name__ == "__main__":
    engine = ProcessingEngine(debug=True)
    engine.turn_on()

    # display each camera connected to the computer with a corrected perspective
    while True:
        frame = engine.get_frame()
        cv2.imshow("CV Module Test", frame)
        print(engine.person_detected())
        if cv2.waitKey(1) & 0xFF == ord('q'):

            break
