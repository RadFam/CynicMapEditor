# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dyn_1-3_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Comm import Communicate

class Ui_Dyn13_widget(QtWidgets.QDialog):

    def __init__(self, yPos, xPos, ttcls, parent=None):
        super().__init__(parent)

        self.lgcCoord = (yPos, xPos)

        self.sd = Communicate()
        self.sd.dyn13_SendData.connect(ttcls.updateDynamicOneThree)

        self.setObjectName("Dyn13_widget")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(278, 151)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(120, 10, 61, 20))
        self.label.setObjectName("label")

        self.OnceReplic = QtWidgets.QTextEdit(self)
        self.OnceReplic.setGeometry(QtCore.QRect(30, 40, 211, 61))
        self.OnceReplic.setObjectName("OnceReplic")

        self.SaveData = QtWidgets.QPushButton(self)
        self.SaveData.setGeometry(QtCore.QRect(180, 120, 75, 23))
        self.SaveData.setObjectName("SaveData")
        self.SaveData.clicked.connect(self.widgetMainMission)

        self.retranslateUi()
        print("Widget is opening")
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def widgetMainMission(self):
        str = self.OnceReplic.toPlainText()
        self.sd.dyn13_SendData.emit(str, self.lgcCoord[0], self.lgcCoord[1])
        self.close()
        return


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dyn13_widget", "Настройки объекта"))
        self.label.setText(_translate("Dyn13_widget", "Реплика"))
        self.SaveData.setText(_translate("Dyn13_widget", "Сохранить"))

