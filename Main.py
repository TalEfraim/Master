import sys
from PyQt5 import QtWidgets as Qtw
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QLabel
import Camera_module
import Logger_module
from FrontEnd_module import Ui_MainWindow


class UI(Qtw.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Available_cameras = QCameraInfo.availableCameras()
        if not self.Available_cameras:
            self.Available_cameras = 0
            WarningMsg = "No available cameras."
            Logger_module.Add_Trace_To_Logfile(WarningMsg, "WARNING")
        self.Video_capture = False
        self.ui.TurnCameraButton.clicked.connect(self.Camera_button_pressed)
        self.ui.TurnCameraButton.clicked.connect(self.Camera_button_pressed)
        self.ui.SetExportPathButton.clicked.connect(self.Set_export_path)
        self.ui.CreateReportButton.clicked.connect(self.Create_report)
        self.Worker1 = Camera_module.Worker1()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

    # will be called when camera button pressed and camera off.
    def ImageUpdateSlot(self, Image):
        self.ui.MainVideo.setPixmap(QPixmap.fromImage(Image))

    # will be called when camera button pressed and camera already on.
    def CancelFeed(self):
        self.Worker1.stop()

    def Set_export_path(self):
        return


    def Create_report(self):
        return

    # @pyqtSlot()
    def Camera_button_pressed(self):
        try:
            if self.Available_cameras != 0 and not self.Video_capture:
                self.Video_capture = True
                Msg = "Camera turned on"
                Logger_module.Add_Trace_To_Logfile(message=Msg, log_mode='INFO')
                Camera_module.Turn_camera_on(self)

            elif self.Available_cameras != 0 and self.Video_capture:
                self.Video_capture = False
                Msg = "Camera turned off"
                Logger_module.Add_Trace_To_Logfile(message=Msg, log_mode='INFO')
                Camera_module.Turn_camera_off(self)
                self.CancelFeed()

        except Exception as ErrorMsg:
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode=ErrorMsg)
            return







if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    window = UI() #Create an instance of our class.
    window.show()
    app.exec_()  #Start the application.