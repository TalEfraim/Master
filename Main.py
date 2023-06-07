import sys
from FrontEnd import Ui_MainWindow
from PyQt5 import QtWidgets as Qtw

class UI(Qtw.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Camera_on = False
        self.ui.TurnCameraButton.clicked.connect(self.Camera_button_pressed)
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
            else:
                self.Camera_on = False
        except Exception as ErrorMsg:
            print(ErrorMsg)
            return







if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    window = UI() #Create an instance of our class.
    window.show()
    app.exec_()  #Start the application.