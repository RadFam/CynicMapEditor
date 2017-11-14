# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dyn_5_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Comm import Communicate


class Ui_Dyn5_widget(QtWidgets.QDialog):

    def __init__(self, yPos, xPos, ttcls, parent=None):
        super().__init__(parent)

        self.lgcCoord = (yPos, xPos)

        self.sd = Communicate()
        self.sd.dyn5_SendData.connect(ttcls.updateDynamicFive)

        self.setObjectName("Dyn5_widget")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(391, 196)

        self.pushOk = QtWidgets.QPushButton(self)
        self.pushOk.setGeometry(QtCore.QRect(300, 160, 75, 23))
        self.pushOk.setObjectName("pushOk")
        self.pushOk.clicked.connect(self.widgetMainMission)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 10, 101, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(240, 15, 131, 21))
        self.label_2.setObjectName("label_2")

        self.FirstReplic = QtWidgets.QTextEdit(self)
        self.FirstReplic.setGeometry(QtCore.QRect(30, 40, 151, 61))
        self.FirstReplic.setObjectName("FirstReplic")

        self.SecondReplic = QtWidgets.QTextEdit(self)
        self.SecondReplic.setGeometry(QtCore.QRect(210, 40, 151, 61))
        self.SecondReplic.setObjectName("SecondReplic")

        self.TakeItem = QtWidgets.QComboBox(self)
        self.TakeItem.setGeometry(QtCore.QRect(30, 120, 151, 22))
        self.TakeItem.setObjectName("TakeItem")
        self.TakeItem.addItem("Blue key")
        self.TakeItem.addItem("Green key")
        self.TakeItem.addItem("Red key")
        self.TakeItem.addItem("Holy Sword")
        self.TakeItem.addItem("Mifril Armour")

        self.retranslateUi()
        print("Widget is opening")
        #self.show()
        # QtCore.QMetaObject.connectSlotsByName(Dyn5_widget) #  Скорее всего, это не нужно

    def widgetMainMission(self):
        str_1 = self.FirstReplic.toPlainText()
        str_2 = self.SecondReplic.toPlainText()
        itemNum = self.TakeItem.currentText()
        self.sd.dyn5_SendData.emit(str_1, str_2, itemNum, self.lgcCoord[0], self.lgcCoord[1])
        self.close()
        return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dyn5_widget", "Настройки объекта"))
        self.pushOk.setText(_translate("Dyn5_widget", "Сохранить"))
        self.label.setText(_translate("Dyn5_widget", "Начальная реплика"))
        self.label_2.setText(_translate("Dyn5_widget", "Конечная реплика"))

