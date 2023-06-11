import sys
from PyQt5 import QtWidgets as Qtw
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QLabel, QFileDialog
import Camera_module
import Logger_module
from FrontEnd_module import Ui_MainWindow

# ==================================================================================================================== #
# TODO: Software front-end / back-end tasks:

# TODO: 1. Write a function that will get a path for images dataset folder and upload the album to dataset label
# TODO: 2. Write a function that synchronizing between dataset scroll bar to radio box.
# TODO: 3. Write general function to handle "about", "policy", etc.. events.
# TODO: 4. Turn black the  live camera screen when camera state is OFF.
# TODO: 5. Handle software crash in case of camera ON + path choose, any other event.
# TODO: 6. Allow camera switching.
# TODO: 7. Write a short user manual.

# ==================================================================================================================== #
# TODO: Algo tasks:

# TODO: 1. Train a model with data set of target / suspect images set
# TODO: 2. Reach high confidence level
# TODO: 3. Write an algorithm that will detect the target alone.
# TODO: 4. Write an algorithm that will detect the target among others.

# ==================================================================================================================== #


class UI(Qtw.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.SoftwareVersion = '1.0.0'
        self.Available_cameras = QCameraInfo.availableCameras()
        if not self.Available_cameras:
            self.Available_cameras = 0
            WarningMsg = "No available cameras."
            Logger_module.Add_Trace_To_Logfile(WarningMsg, "WARNING")
        self.Video_capture = False
        self.output_directory_path = None
        self.ui.TurnCameraButton.clicked.connect(self.Camera_button_pressed)
        self.ui.TurnCameraButton.clicked.connect(self.Camera_button_pressed)
        self.ui.SetExportPathButton.clicked.connect(self.Set_export_path)
        self.ui.CreateReportButton.clicked.connect(self.Create_report)
        self.Worker1 = Camera_module.Worker1()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

    def ImageUpdateSlot(self, Image):
        self.ui.MainVideo.setPixmap(QPixmap.fromImage(Image))

    def Set_export_path(self):
        try:
            self.output_directory_path = QFileDialog.getExistingDirectory(self,
                                                                        "Please choose output location or create one.")
            if self.output_directory_path:
                self.ui.ExportPathLabel.setText(str(self.output_directory_path))
                Msg = 'Output directory selected. [' + str(self.output_directory_path) + ']'
                Logger_module.Add_Trace_To_Logfile(message=Msg, log_mode='INFO')
            else:
                ErrorMsg = "The selected path isn't valid or unreachable. please choose a proper directory."
                Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='ERROR')
                return
        except:
            ErrorMsg = 'Exception or fatal error in Set_export_path()'
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='CRITICAL')

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

        except Exception as ErrorMsg:
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode=ErrorMsg)
            return


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    window = UI()  # Create an instance of our class.
    window.show()
    app.exec_()  # Start the application.
