import os
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Logger_module
import Main


class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def __init__(self, WhichCameraIndex):
        super().__init__()
        self.camera_index = WhichCameraIndex
        self.threadActive = False

    def run(self):
        try:
            self.ThreadActive = True
            Capture = cv2.VideoCapture(0)
            while self.ThreadActive:
                ret, frame = Capture.read()
                if ret:
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(Image, 1)
                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1],
                                               FlippedImage.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
        except Exception as ErrorMsg:
            Logger_module.Add_Trace_To_Logfile(ErrorMsg, log_mode='ERROR')
            return

    def stop(self):
        self.ThreadActive = False


def Turn_camera_on(self, WhichCameraIndex):
    self.Worker1 = Worker1(WhichCameraIndex=WhichCameraIndex)
    self.Worker1.start()


def Turn_camera_off(self):
    self.Worker1.stop()
