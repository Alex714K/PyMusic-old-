# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mysetting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainSetting(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 191, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_red = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.left_red.setObjectName("left_red")
        self.horizontalLayout.addWidget(self.left_red)
        self.lineRed = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineRed.setObjectName("lineRed")
        self.horizontalLayout.addWidget(self.lineRed)
        self.right_red = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.right_red.setObjectName("right_red")
        self.horizontalLayout.addWidget(self.right_red)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_green = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.left_green.setObjectName("left_green")
        self.horizontalLayout_3.addWidget(self.left_green)
        self.lineGreen = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineGreen.setObjectName("lineGreen")
        self.horizontalLayout_3.addWidget(self.lineGreen)
        self.right_green = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.right_green.setObjectName("right_green")
        self.horizontalLayout_3.addWidget(self.right_green)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_blue = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.left_blue.setObjectName("left_blue")
        self.horizontalLayout_2.addWidget(self.left_blue)
        self.lineBlue = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineBlue.setObjectName("lineBlue")
        self.horizontalLayout_2.addWidget(self.lineBlue)
        self.right_blue = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.right_blue.setObjectName("right_blue")
        self.horizontalLayout_2.addWidget(self.right_blue)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(25, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 190, 421, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.derectory = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.derectory.setObjectName("derectory")
        self.horizontalLayout_4.addWidget(self.derectory)
        self.change_folder = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.change_folder.setText("")
        self.change_folder.setObjectName("change_folder")
        self.horizontalLayout_4.addWidget(self.change_folder)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Цвет фона</p></body></html>"))
        self.left_red.setText(_translate("MainWindow", "<"))
        self.lineRed.setText(_translate("MainWindow", "255"))
        self.right_red.setText(_translate("MainWindow", ">"))
        self.label_2.setText(_translate("MainWindow", "Red"))
        self.left_green.setText(_translate("MainWindow", "<"))
        self.lineGreen.setText(_translate("MainWindow", "255"))
        self.right_green.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "Green"))
        self.left_blue.setText(_translate("MainWindow", "<"))
        self.lineBlue.setText(_translate("MainWindow", "255"))
        self.right_blue.setText(_translate("MainWindow", ">"))
        self.label_4.setText(_translate("MainWindow", "Blue"))