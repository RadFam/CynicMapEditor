# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dyn_4_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Comm import Communicate


class Ui_Dyn4_widget(QtWidgets.QDialog):

    def __init__(self, yPos, xPos, ttcls, parent=None):
        super().__init__(parent)

        self.lgcCoord = (yPos, xPos)

        self.sd = Communicate()
        self.sd.dyn4_SendData.connect(ttcls.updateDynamicFour)

        self.setObjectName("Dyn4_widget")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(443, 216)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 20, 111, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 121, 16))
        self.label_2.setObjectName("label_2")

        self.FirstReplic = QtWidgets.QTextEdit(self)
        self.FirstReplic.setGeometry(QtCore.QRect(20, 50, 181, 61))
        self.FirstReplic.setObjectName("FirstReplic")

        self.SecondReplic = QtWidgets.QTextEdit(self)
        self.SecondReplic.setGeometry(QtCore.QRect(240, 50, 181, 61))
        self.SecondReplic.setObjectName("SecondReplic")

        self.TakeItem = QtWidgets.QComboBox(self)
        self.TakeItem.setGeometry(QtCore.QRect(20, 130, 181, 22))
        self.TakeItem.setObjectName("TakeItem")
        self.TakeItem.addItem("Blue key")
        self.TakeItem.addItem("Green key")
        self.TakeItem.addItem("Red key")
        self.TakeItem.addItem("Holy Sword")
        self.TakeItem.addItem("Mifril Armour")

        self.GiveItem = QtWidgets.QComboBox(self)
        self.GiveItem.setGeometry(QtCore.QRect(240, 130, 181, 22))
        self.GiveItem.setObjectName("GiveItem")
        self.GiveItem.addItem("Blue key")
        self.GiveItem.addItem("Green key")
        self.GiveItem.addItem("Red key")
        self.GiveItem.addItem("Holy Sword")
        self.GiveItem.addItem("Mifril Armour")

        self.AddChain = QtWidgets.QPushButton(self)
        self.AddChain.setGeometry(QtCore.QRect(250, 170, 81, 23))
        self.AddChain.setObjectName("AddChain")
        self.AddChain.clicked.connect(self.addScenarioChain)

        self.SaveData = QtWidgets.QPushButton(self)
        self.SaveData.setGeometry(QtCore.QRect(340, 170, 81, 23))
        self.SaveData.setObjectName("SaveData")
        self.SaveData.clicked.connect(self.widgetMainMission)

        self.retranslateUi()
        print("Widget is opening")
        #self.show()
        #QtCore.QMetaObject.connectSlotsByName(Form)

    def addScenarioChain(self):
        str_1 = self.FirstReplic.toPlainText()
        str_2 = self.SecondReplic.toPlainText()
        itemNum_t = self.TakeItem.currentText()
        itemNum_g = self.GiveItem.currentText()
        self.sd.dyn4_SendData.emit(str_1, str_2, itemNum_t, itemNum_g, self.lgcCoord[0], self.lgcCoord[1])
        return

    def widgetMainMission(self):
        self.close()
        return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dyn4_widget", "Настройки объекта"))
        self.label.setText(_translate("Dyn4_widget", "Начальная реплика"))
        self.label_2.setText(_translate("Dyn4_widget", "Конечная реплика"))
        self.AddChain.setText(_translate("Dyn4_widget", "Добавить"))
        self.SaveData.setText(_translate("Dyn4_widget", "Сохранить"))

