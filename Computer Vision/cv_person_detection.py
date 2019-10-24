"""
Contains all the classes used for computer vision and backend processing.

@author: Duncan Mazza
Stripped down for Raspi by Michael Remley
@revision: v1.4
"""
# pip install opencv-python
# pip install opencv-contrib-python
import cv2
import cv2.aruco as aruco
from math import acos, cos, sin
import numpy as np
import os

DETECTION_THRESHOLD = 0.6  # minimum confidence level for person to be recognized

class ProcessingEngine:
    """
    The backend class for image per-processing.
    """

    def __init__(self, threshold=30, debug=False):
        # load the COCO class labels our YOLO model was trained on
        cwd = os.getcwd()
        print(cwd)
        if __name__ == '__main__':
            labelsPath = os.path.sep.join(["yolo-coco","coco.names"])

            self.weightsPath = os.path.sep.join([cwd, 'yolo-coco', "yolov3.weights"])
            self.configPath = os.path.sep.join([cwd, 'yolo-coco', "yolov3.cfg"])
        else:
            labelsPath = os.path.sep.join(["api","yolo-coco","coco.names"])

            self.weightsPath = os.path.sep.join([cwd, 'api/yolo-coco', "yolov3.weights"])
            self.configPath = os.path.sep.join([cwd, 'api/yolo-coco', "yolov3.cfg"])

        self.LABELS = open(labelsPath).read().strip().split("\n")

        self.ln = 0  # a placeholder (for determining only the *output* layer names that we need from YOLO)
        # that is overridden when self.turn_on() is called

        self.n = 0  # counter for the calibration process
        self.threshold = threshold  # minimum number of frames used to perform calibration
        self.matrix_list = []  # used to store matrices during calibration
        # initialize parameters for ARUCO detection (used for perspective correction)
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.parameters = aruco.DetectorParameters_create()

        self.debug = debug

        self.cap_dict = {}  # store the OpenCV captures in a dictionary
        self.detect_dict = {}  # store detected outputs in a dictionary
        self.num_caps = 0  # initialize the value that stores the number of OpenCV captures

        self.cap_num_dict = {1: (320, 320), 2: (128, 128), 3: (96, 96)}

    def turn_on(self, filename=''):
        """
        This method loads all of the OpenCV camera captures into self.cap_dict and, and also loads all of the
        objects used for detection and stores them in self.detect_dict. One of the main purposes of this function is
        so that the camera(s) is/are not turned on until the select_feeds.html file is opened.
        :param filename: path to the video file being uploaded if not using the live camera footage
        :return:
        """
        i = 0  # counter used for indexing
        # If a filename is specified, do no camera feeds.
        if filename != '':
            cap = cv2.VideoCapture(filename)
            if cap.isOpened():
                # Representation of dictionary entries: [OpenCV capture, calibration boolean, 0 which is a placeholder
                # for the calibration matrix, 1, which is boolean for whether the camera is to be used, and (height,
                # width) of the camera frame]
                print(type(self.cap_dict))
                self.cap_dict[i] = [cap, 0, 0, 1, (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                                                   int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))]
                print("[INFO] loading YOLO from disk for file {}...".format(filename))
                self.detect_dict[i] = cv2.dnn.readNetFromDarknet(self.configPath,
                                                                 self.weightsPath)  # load our YOLO object detector trained on COCO dataset (80 classes)
                print("[INFO] finished loading YOLO for file {}...".format(filename))
                if i == 0:  # the following part only needs to be initialized once, but it is in this for loop because
                    #  the at least one cv2.dnn.readNetFromDarknet(...) has to have been initialized for this part to
                    # be initialized.

                    # determine only the *output* layer names that we need from YOLO
                    self.ln = self.detect_dict[i].getLayerNames()
                    self.ln = [self.ln[i[0] - 1] for i in self.detect_dict[i].getUnconnectedOutLayers()]
                    self.num_caps = 1
                    return
            else:  # The file did not load correctly
                # TODO: Handle this case better
                self.num_caps = 0
                return
        else:  # using live footage from the cameras connected to the computer
            # add all of the OpenCV captures to self.cap_dict:
            while i < 5:  # support up to 5 different cameras
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    # Representation of dictionary entries: [OpenCV capture, calibration boolean, 0 which is a placeholder
                    # for the calibration matrix, 1, which is boolean for whether the camera is to be used, and (height,
                    # width) of the camera frame]
                    self.cap_dict[i] = [cap, 0, 0, 1, (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                                                       int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))]
                    print("[INFO] loading YOLO from disk for camera {}...".format(i))
                    self.detect_dict[i] = cv2.dnn.readNetFromDarknet(self.configPath,
                                                                     self.weightsPath)  # load our YOLO object detector trained on COCO dataset (80 classes)
                    print("[INFO] finished loading YOLO for camera {}...".format(i))
                    if i == 0:  # the following part only needs to be initialized once, but it is in this for loop because
                        #  the at least one cv2.dnn.readNetFromDarknet(...) has to have been initialized for this part to
                        # be initialized.

                        # determine only the *output* layer names that we need from YOLO
                        self.ln = self.detect_dict[i].getLayerNames()
                        self.ln = [self.ln[i[0] - 1] for i in self.detect_dict[i].getUnconnectedOutLayers()]

                else:  # all the cameras that can be detected have been, so break the loop:
                    self.num_caps = i
                    break
                i += 1

    def turn_off(self, reset_detection=True):
        """
        Releases all of the OpenCV captures and clears the appropriate attributes from the class.
        :return: void
        """

        # TODO: currently not used...
        for i in range(self.num_caps):
            cap = self.cap_dict[i]
            cap[0].release()

        self.cap_dict = {}
        self.num_caps = 0

        if reset_detection:
            self.detect_dict = {}
            self.ln = 0

    def _parse_detected(self, frame, layerOutputs, cap_num):
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
        W = self.cap_dict[cap_num][4][1]
        H = self.cap_dict[cap_num][4][0]

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
                if confidence > DETECTION_THRESHOLD:
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
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, DETECTION_THRESHOLD, 0.3)

        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                if self.LABELS[classIDs[i]] != 'person':
                    frame_copy = frame
                    return [], frame_copy
                else:
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
        frame_copy = frame
        return boxes, frame_copy

    def get_frame(self, cap_num, calibrate=False):
        """
        Returns the captured frame that is warped by the calibration_matrix
        :param: cap_num - index number of the OpenCV capture
        :param: calibrate - boolean for whether the frame should be perspective corrected
        :return: frame or frame converted to bytes, depending on use case
        """
        # if the camera is set to off, then dim the frame by x0.2

        cap = self.cap_dict.get(cap_num)[0]  # select the camera from self.cap_dict
        _, frame = cap.read()  # read the camera capture

        # pull out the height and width of the camera frame
        height = self.cap_dict[cap_num][4][0]
        width = self.cap_dict[cap_num][4][1]

        if self.cap_dict[cap_num][3] == 0:  # if the camera is muted
            frame = frame * 0.2  # dim the camera feed
            return frame if self.debug else cv2.imencode('.jpg', frame)[1].tobytes()  # perform no further computation

        else:  # if the camera is not muted:
            if self.cap_dict[cap_num][1] == 1 or calibrate == True:  # if the camera is in calibration mode:
                if type(self.cap_dict[cap_num][2]) != int:  # already calibrated if true; compare type because when it
                    # becomes the calibration matrix, the truth value of a multi-element array is ambiguous
                    frame = cv2.warpPerspective(frame, self.cap_dict[cap_num][2], (height, width))
                else:  # perform calibration
                    while self.cap_dict[cap_num][2] == 0:  # not yet calibrated
                        frame = self.calibrate(cap_num, frame)
                        return frame if self.debug else cv2.imencode('.jpg', frame)[1].tobytes()

            else:  # if the camera is not in calibration mode, perform the person detection
                net = self.detect_dict[cap_num]  # select the image processor (net)
                blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, self.cap_num_dict[self.num_caps],
                                             swapRB=True, crop=False)  # pre=process the image for detection

                # run detection on the frame:
                net.setInput(blob)
                layerOutputs = net.forward(self.ln)
                boxes, frame = self._parse_detected(frame, layerOutputs, cap_num)

                return frame if self.debug else cv2.imencode('.jpg', frame)[1].tobytes()

if __name__ == "__main__":
    engine = ProcessingEngine(debug=True)
    engine.turn_on()

    # display each camera connected to the computer with a corrected perspective
    while True:
        for cap_num in range(engine.num_caps):
            frame = engine.get_frame(cap_num, calibrate=False)
            cv2.imshow("frame {}".format(cap_num), frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):

                break
