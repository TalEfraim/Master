import os
import cv2
import sys
import Logger_module
from PyQt5.QtMultimedia import *
from PyQt5 import QtWidgets as Qtw
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from FrontEnd_module import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QAction
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt, QMutex, QWaitCondition

# ==================================================================================================================== #
# TODO: Software front-end / back-end tasks:

# TODO: 1. Handle camera thread in re-flow
# TODO: 2. Turn black the  live camera screen when camera state is OFF.
# TODO: 3. Handle software crash in case of camera ON + path choose, any other event.

# ==================================================================================================================== #
# TODO: Algo tasks:

# TODO: 1. Train a model with data set of target / suspect images set
# TODO: 2. Reach high confidence level
# TODO: 3. Write an algorithm that will detect the target alone.
# TODO: 4. Write an algorithm that will detect the target among others.

# ==================================================================================================================== #

def load_file_content(Filename):
    file_contents = ''
    with open(Filename, 'r') as file:
        file_contents = file.read()
    return file_contents


class CamThread(QThread):
    changemap = pyqtSignal('QImage')

    def __init__(self, mutex, condition, camera_idx):
        super().__init__()
        self.mutex = mutex
        self.condition = condition
        self.running = True
        self.CamIDX = camera_idx

    def run(self):
        cap = cv2.VideoCapture(self.CamIDX)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        while self.running:
            try:
                ret, img_rgb = cap.read()
                if ret:
                    rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

                    # any other image processing here

                    convert = QImage(rgb.data, rgb.shape[1], rgb.shape[0], QImage.Format_RGB888)
                    p = convert.scaled(640, 480, Qt.KeepAspectRatio)
                    self.changemap.emit(p)
                    self.condition.wait(self.mutex)

            except Exception as ErrorMsg:
                Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='ERROR')

    def stop(self):
        self.running = False


class UI(Qtw.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.thr = None
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.ThreadExist = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected_camera_index = 0
        self.ImagesList = None
        self.SoftwareVersion = '1.0.0'
        self.Policy_content = load_file_content('Policy.txt')
        self.SoftwareINFO_content =load_file_content('Software info.txt')
        self.ui.actionversion_number.setText(self.SoftwareVersion)
        self.Available_cameras = QCameraInfo.availableCameras()
        if not self.Available_cameras:
            self.Available_cameras = 0
            WarningMsg = "No available cameras."
            Logger_module.Add_Trace_To_Logfile(WarningMsg, "WARNING")
        elif len(self.Available_cameras) > 0:
            for camera in self.Available_cameras:
                action = QAction(camera.description(), self.ui.menuChoose_camera)
                action.triggered.connect(lambda _, cam=camera: self.select_camera(cam))
                self.ui.menuChoose_camera.addAction(action)
        self.Video_capture = False
        self.output_directory_path = None
        self.ui.actionLoad_target_images.triggered.connect(self.Load_Dataset)
        self.ui.actionPolicy_2.triggered.connect(self.Present_policy)
        self.ui.actionSofware_info.triggered.connect(self.Present_Sofware_info)
        self.ui.CurrentImage_slider.valueChanged.connect(self.Value_changed_ImageSlider)
        self.ui.CurrentImage_radiobox.valueChanged.connect(self.Value_changed_ImageRadiobox)
        self.ui.CameraOnBtn.clicked.connect(self.CameraON)
        self.ui.CameraOffBtn.clicked.connect(self.CameraOFF)
        self.ui.SetExportPathButton.clicked.connect(self.Set_export_path)
        self.ui.CreateReportButton.clicked.connect(self.Create_report)
        self.ui.MainVideo.setPixmap(QPixmap('camera off icon.png'))
        self.Data_set = []


    def CameraON(self): #why the hell it crashing in second time ?!!
        self.mutex.lock()
        self.thr = CamThread(mutex=self.mutex, condition=self.condition, camera_idx=self.selected_camera_index)
        self.thr.changemap.connect(self.ImageUpdateSlot)
        self.thr.start()
        self.ThreadExist = True

    def CameraOFF(self):
        if self.ThreadExist:
            self.thr.stop()
            self.ThreadExist = False
            del self.thr
            pixmap = QPixmap('camera off icon.png')
            self.ui.MainVideo.setPixmap(pixmap)


    def select_camera(self, camera):
        selected_index = QCameraInfo.availableCameras().index(camera)
        self.selected_camera_index = selected_index

    @pyqtSlot('QImage')
    def ImageUpdateSlot(self, Image):
        self.mutex.lock()
        try:
            self.ui.MainVideo.setPixmap(
                QPixmap.fromImage(Image))  # I think this line causing the crash after video stop.
        finally:
            self.mutex.unlock()
            self.condition.wakeAll()

        # except Exception as ErrorMsg:
        #     Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='ERROR')

    def Load_Dataset(self):
        Input_folder = QFileDialog.getExistingDirectory(self, "Please choose images location directory.")
        self.ImagesList = [f for f in os.listdir(Input_folder) if f.endswith('.jpg')]
        for image in self.ImagesList:
            pixmap = QPixmap(os.path.join(Input_folder, image))
            self.Data_set.append(pixmap)

    def Refresh_view(self, image_idx):
        if len(self.Data_set) == 0:
            return
        else:
            pixmap = self.Data_set[image_idx]
            label_width = self.ui.DatasetImages.width()
            label_height = self.ui.DatasetImages.height()

            scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.IgnoreAspectRatio)
            self.ui.DatasetImages.setPixmap(scaled_pixmap)
            self.ui.DatasetImages.update()
            self.ui.CurrentImage_slider.setMaximum(len(self.Data_set) - 1)
            self.ui.CurrentImage_radiobox.setMaximum(len(self.Data_set) - 1)


    def Value_changed_ImageSlider(self):
        try:
            plot_box = self.ui.CurrentImage_radiobox.value()
            plot_slider = self.ui.CurrentImage_slider.value()
            if plot_box != plot_slider:
                self.ui.CurrentImage_radiobox.setValue(plot_slider)
                self.Refresh_view(image_idx=plot_slider)
        except Exception as ErrorMsg:
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='ERROR')
            return

    def Value_changed_ImageRadiobox(self):
        try:
            plot_box = self.ui.CurrentImage_radiobox.value()
            plot_slider = self.ui.CurrentImage_slider.value()
            if plot_box != plot_slider:
                self.ui.CurrentImage_slider.setValue(plot_box)
                self.Refresh_view(image_idx=plot_box)
        except Exception as ErrorMsg:
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='ERROR')
            return

    def Popup_a_message(self, popup_title, popup_content):
        popup = QMessageBox()
        popup.setWindowTitle(popup_title)
        popup.setText(popup_content)
        popup.exec_()

    def Present_policy(self):
        self.Popup_a_message(popup_title='Policy', popup_content=self.Policy_content)

    def Present_Sofware_info(self):
        self.Popup_a_message(popup_title='Software info', popup_content=self.SoftwareINFO_content)

    def Set_export_path(self):
        try:
            self.output_directory_path = QFileDialog.getExistingDirectory(self,
                                                                          "Please choose output location or create one.")
            if self.output_directory_path:
                self.ui.ExportPathLabel.setText(str(self.output_directory_path))
                Msg = 'Output directory selected. [' + str(self.output_directory_path) + ']'
                Logger_module.Add_Trace_To_Logfile(message=Msg, log_mode='INFO')
            else:
                WarningMsg = "The selected path isn't valid or unreachable. please choose a proper directory."
                Logger_module.Add_Trace_To_Logfile(message=WarningMsg, log_mode='WARNING')
                return
        except:
            ErrorMsg = 'Exception or fatal error in Set_export_path()'
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode='CRITICAL')

    def Create_report(self):
        return


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    window = UI()  # Create an instance of our class.
    window.show()
    app.exec_()  # Start the application.
