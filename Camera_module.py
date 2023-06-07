# This module is activating the web-camera. Escape pressing will shut it down.
import cv2


class CAMERA:
    def __init__(self):
        self.Video_window = cv2.namedWindow("preview")
        self.Video_capture = cv2.VideoCapture(0)
        if self.Video_capture.isOpened():
            self.rval, self.frame = self.Video_capture.read()
        else:
            self.rval = False

    def Run(self):
        while self.rval:
            cv2.imshow("preview", self.frame)
            self.rval, self.frame = self.Video_capture.read()
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break

