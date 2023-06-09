import sys
from FrontEnd_module import Ui_MainWindow
import Logger_module
import Camera_module
from functools import partial
from PyQt5 import QtWidgets as Qtw


class UI(Qtw.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Camera_on = False
        self.ui.TurnCameraButton.clicked.connect(partial(self.Camera_button_pressed, "on"))
        self.ui.TurnCameraButton.clicked.connect(partial(self.Camera_button_pressed, "off"))
        self.ui.SetExportPathButton.clicked.connect(self.Set_export_path)
        self.ui.CreateReportButton.clicked.connect(self.Create_report)

    def Set_export_path(self):
        return


    def Create_report(self):
        return


    def Camera_button_pressed(self):
        try:
            if not self.Camera_on:
                self.Camera_on = True
                Msg = "Camera turned on"
                Logger_module.Add_Trace_To_Logfile(message=Msg, log_mode='INFO')
            else:
                self.Camera_on = False
                Msg = "Camera turned off"
                Logger_module.Add_Trace_To_Logfile(message=Msg, log_mode='INFO')

        except Exception as ErrorMsg:
            Logger_module.Add_Trace_To_Logfile(message=ErrorMsg, log_mode=ErrorMsg)
            return







if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    window = UI() #Create an instance of our class.
    window.show()
    app.exec_()  #Start the application.