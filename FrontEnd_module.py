# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frontend.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TurnCameraButton = QtWidgets.QPushButton(self.centralwidget)
        self.TurnCameraButton.setGeometry(QtCore.QRect(130, 340, 131, 31))
        self.TurnCameraButton.setObjectName("TurnCameraButton")
        self.TargetImagesLabel = QtWidgets.QLabel(self.centralwidget)
        self.TargetImagesLabel.setGeometry(QtCore.QRect(560, 15, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TargetImagesLabel.setFont(font)
        self.TargetImagesLabel.setObjectName("TargetImagesLabel")
        self.CurrentImage_slider = QtWidgets.QSlider(self.centralwidget)
        self.CurrentImage_slider.setGeometry(QtCore.QRect(540, 280, 191, 20))
        self.CurrentImage_slider.setOrientation(QtCore.Qt.Horizontal)
        self.CurrentImage_slider.setObjectName("CurrentImage_slider")
        self.CurrentImage_radiobox = QtWidgets.QSpinBox(self.centralwidget)
        self.CurrentImage_radiobox.setGeometry(QtCore.QRect(740, 280, 42, 22))
        self.CurrentImage_radiobox.setObjectName("CurrentImage_radiobox")
        self.CreateReportButton = QtWidgets.QPushButton(self.centralwidget)
        self.CreateReportButton.setGeometry(QtCore.QRect(580, 510, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CreateReportButton.setFont(font)
        self.CreateReportButton.setStyleSheet("background-color: rgb(225,220,220);")
        self.CreateReportButton.setObjectName("CreateReportButton")
        self.ExportPathLabel = QtWidgets.QLabel(self.centralwidget)
        self.ExportPathLabel.setGeometry(QtCore.QRect(160, 472, 641, 31))
        self.ExportPathLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.ExportPathLabel.setText("")
        self.ExportPathLabel.setObjectName("ExportPathLabel")
        self.SetExportPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetExportPathButton.setGeometry(QtCore.QRect(20, 460, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SetExportPathButton.setFont(font)
        self.SetExportPathButton.setObjectName("SetExportPathButton")
        self.MainVideo = QtWidgets.QLabel(self.centralwidget)
        self.MainVideo.setGeometry(QtCore.QRect(30, 20, 351, 311))
        self.MainVideo.setStyleSheet("background-color: rgb(225,220,220);")
        self.MainVideo.setText("")
        self.MainVideo.setObjectName("MainVideo")
        self.DatasetImages = QtWidgets.QLabel(self.centralwidget)
        self.DatasetImages.setGeometry(QtCore.QRect(540, 50, 241, 221))
        self.DatasetImages.setStyleSheet("background-color: rgb(225,220,220);")
        self.DatasetImages.setText("")
        self.DatasetImages.setObjectName("DatasetImages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuChoose_camera = QtWidgets.QMenu(self.menuMenu)
        self.menuChoose_camera.setObjectName("menuChoose_camera")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuVersion = QtWidgets.QMenu(self.menuAbout)
        self.menuVersion.setObjectName("menuVersion")
        self.menuSoftware_manual = QtWidgets.QMenu(self.menubar)
        self.menuSoftware_manual.setObjectName("menuSoftware_manual")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_target_images = QtWidgets.QAction(MainWindow)
        self.actionLoad_target_images.setObjectName("actionLoad_target_images")
        self.actionPolicy = QtWidgets.QAction(MainWindow)
        self.actionPolicy.setObjectName("actionPolicy")
        self.actionPolicy_2 = QtWidgets.QAction(MainWindow)
        self.actionPolicy_2.setObjectName("actionPolicy_2")
        self.actionSofware_info = QtWidgets.QAction(MainWindow)
        self.actionSofware_info.setObjectName("actionSofware_info")
        self.actionversion_number = QtWidgets.QAction(MainWindow)
        self.actionversion_number.setObjectName("actionversion_number")
        self.actionf = QtWidgets.QAction(MainWindow)
        self.actionf.setObjectName("actionf")
        self.menuMenu.addAction(self.actionLoad_target_images)
        self.menuMenu.addAction(self.menuChoose_camera.menuAction())
        self.menuVersion.addAction(self.actionversion_number)
        self.menuAbout.addAction(self.menuVersion.menuAction())
        self.menuAbout.addAction(self.actionSofware_info)
        self.menuAbout.addAction(self.actionPolicy_2)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuSoftware_manual.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Suspect detector"))
        self.TurnCameraButton.setText(_translate("MainWindow", "Camera ON/OFF"))
        self.TargetImagesLabel.setText(_translate("MainWindow", "Target images database:"))
        self.CreateReportButton.setText(_translate("MainWindow", "Create target report"))
        self.SetExportPathButton.setText(_translate("MainWindow", "Set output path"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuChoose_camera.setTitle(_translate("MainWindow", "Choose camera"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuVersion.setTitle(_translate("MainWindow", "Version"))
        self.menuSoftware_manual.setTitle(_translate("MainWindow", "Software manual"))
        self.actionLoad_target_images.setText(_translate("MainWindow", "Load target images"))
        self.actionPolicy.setText(_translate("MainWindow", "Policy"))
        self.actionPolicy_2.setText(_translate("MainWindow", "Policy"))
        self.actionSofware_info.setText(_translate("MainWindow", "Sofware info"))
        self.actionversion_number.setText(_translate("MainWindow", "Version_number"))
        self.actionf.setText(_translate("MainWindow", "f"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
