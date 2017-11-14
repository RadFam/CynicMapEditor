# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QListView, QListWidget, QListWidgetItem
from PyQt5.QtCore import QPoint, QSize, Qt
from TotalControl import TCL
from Comm import Communicate

import Dyn_5_widget

# Класс модифицированного лейбла
class ModLabel(QtWidgets.QLabel):
    
    def __init__(self, xC, yC, tcl, updlg, parent=None):
        super(ModLabel, self).__init__(parent)
        self.xx = xC
        self.yy = yC
        self.logX = int(xC/60)
        self.logY = int(yC/60)
        self.ttc = tcl  # Скорее всего, это передавать не нужно вообще
        self.pb1 = Communicate()
        self.pb2 = Communicate()
        self.pb1.lbClickData_lbl.connect(updlg.changeObj)
        self.pb2.rbClickData_lbl.connect(updlg.modifyObj)


    def mousePressEvent(self, event):
        self.xPos = event.pos().x() + self.xx
        self.yPos = event.pos().y() + self.yy
        self.logX = int(self.xPos/60)
        self.logY = int(self.yPos/60)
        if event.button() == 1:  # Нажали левую кнопку
            self.pb1.lbClickData_lbl.emit(self.logX, self.logY)
            return
        if event.button() == 2:  # Нажали правую кнопку
            self.pb2.rbClickData_lbl.emit(self.logX, self.logY)
            return

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.lastPos = QPoint()
        self.totalctrl = TCL(self)
        self.ModLabs = [[0] * self.totalctrl.LabWidth for i in range(self.totalctrl.LabHeight)]

        self.cntr = 0
        self.objectSelected = 1

        self.lc = Communicate()  # Левый клик
        self.rc = Communicate()  # Правый клик
        self.sv = Communicate()
        self.ld = Communicate()
        self.lc.lbClickData_dlg.connect(self.totalctrl.changeElement)
        self.rc.rbClickData_dlg.connect(self.totalctrl.modifyElement)
        self.sv.saveFile.connect(self.totalctrl.SaveObjMatrix)
        self.ld.loadFile.connect(self.totalctrl.LoadObjMatrix)

        self.base_width = 31
        self.base_height = 31

        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        # Добавляем область для рисования нашей карты
        self.scrlDrawArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrlDrawArea.setGeometry(QtCore.QRect(10, 10, 510, 510))
        self.scrlDrawArea.setWidgetResizable(True)
        self.scrlDrawArea.setFixedHeight(540)
        self.scrlDrawArea.setFixedWidth(540)
        self.scrlDrawArea.setObjectName("scrlDrawArea")

        # Это для отрисовки тайлов внутри scrollbarArea
        self.drawLayout = QtWidgets.QGridLayout()
        self.drawLayout.setContentsMargins(0, 0, 0, 0)
        self.drawLayout.setVerticalSpacing(0)
        self.drawLayout.setHorizontalSpacing(0)
        self.drawGroupBox = QtWidgets.QGroupBox()

        # Тут у нас будет поле ввода для высоты карты
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(575, 10, 75, 23))
        self.label.setObjectName("label")
        self.label.setText("Высота поля")

        self.txted_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txted_1.setGeometry(QtCore.QRect(570, 40, 75, 23))
        self.txted_1.setObjectName("txted_1")
        self.txted_1.setText(str(self.base_height))

        # Тут у нас будет поле ввода для ширины карты
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(665, 10, 75, 23))
        self.label_2.setObjectName("label")
        self.label_2.setText("Ширина поля")

        self.txted_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txted_2.setGeometry(QtCore.QRect(660, 40, 75, 23))
        self.txted_2.setObjectName("txted_1")
        self.txted_2.setText(str(self.base_width))

        # Тепрь это у нас будет кнопка с функцией "Сгенеировать первичный лабиринт"
        self.gnrtBtn = QtWidgets.QPushButton(self.centralwidget)
        self.gnrtBtn.setGeometry(QtCore.QRect(570, 70, 75, 23))
        self.gnrtBtn.setObjectName("gnrtBtn")
        self.gnrtBtn.clicked.connect(self.getNewMap)

        # Тут будет кнопка для генерации пустой площадки для лабиринта
        self.bsgenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.bsgenBtn.setGeometry(QtCore.QRect(660, 70, 75, 23))
        self.bsgenBtn.setObjectName("bsgenBtn")
        self.bsgenBtn.clicked.connect(self.getNewMapSmpl)


        # Здесь будет кнопка с функцией "Загрузить"
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn.setGeometry(QtCore.QRect(570, 100, 75, 23))
        self.loadBtn.setObjectName("loadBtn")
        self.loadBtn.clicked.connect(self.LoadMapIntoFile)

        # Здесь у нас будет кнопка с функцией "Сохранить"
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(660, 100, 75, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(self.SaveMapIntoFile)

        # Здесь будет виджет для выбора объекта игрового мира
        self.contentsWidget = QListWidget(self.centralwidget)
        self.contentsWidget.setViewMode(QListView.IconMode)
        self.contentsWidget.setIconSize(QSize(96, 84))
        self.contentsWidget.setMovement(QListView.Static)
        self.contentsWidget.setMaximumWidth(210)
        self.contentsWidget.setMaximumHeight(430)
        self.contentsWidget.setSpacing(12)
        self.contentsWidget.setGeometry(QtCore.QRect(570, 130, 210, 430))
        self.createIcons()
        self.contentsWidget.setCurrentRow(0)
        self.contentsWidget.currentItemChanged.connect(self.selectObj)

        # Меню и статусбары, который все равно не отрабатываются - надо их удалить
        self.setCentralWidget(self.centralwidget)
        #  self.menubar = QtWidgets.QMenuBar()
        #  self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        #  self.menubar.setObjectName("menubar")
        #  self.setMenuBar(self.menubar)
        #  self.statusbar = QtWidgets.QStatusBar()
        #  self.statusbar.setObjectName("statusbar")
        #  self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.show()
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Изменился объект игрового поля
    def changeObj(self, yP, xP):
        self.lc.lbClickData_dlg.emit(yP, xP, self.objectSelected)
        return

    # Модифицировался объект игрового поля
    def modifyObj(self, yP, xP):
        self.rc.rbClickData_dlg.emit(yP, xP)
        return

    # Заполняем поле выбора элементов, объектами игрового поля
    def selectObj(self, current, previous):
        if not current:
            current = previous
        self.objectSelected = self.contentsWidget.row(current) + 1

    def createIcons(self):
        for ii in range(1, len(self.totalctrl.ObjectList)):
            configButton = QListWidgetItem(self.contentsWidget)
            configButton.setIcon(QtGui.QIcon(self.totalctrl.ObjectList[ii].csSprite))
            configButton.setText(self.totalctrl.ObjectList[ii].csName)
            configButton.setTextAlignment(Qt.AlignHCenter)
            configButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        return

    # Сохранение текущей карты
    def SaveMapIntoFile(self):
        # Надо вызвать диалоговое окно выбора сохраненного файла
        f = QtWidgets.QFileDialog.getSaveFileName(parent=self, caption="Сохранить файл",
                                                  directory=QtCore.QDir.currentPath(),
                                                  filter="Save File (*.crm)",
                                                  initialFilter="Save File (*.crm)")
        if len(f[0]) > 0:
            self.sv.saveFile.emit(f[0])

        return

    def LoadMapIntoFile(self):
        f = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption="Открыть файл",
                                                  directory=QtCore.QDir.currentPath(),
                                                  filter="Load File (*.crm)",
                                                  initialFilter="Load File (*.crm)")
        if len(f[0]) > 0:
            self.ld.loadFile.emit(f[0])
            self.drawPictures()

        return

    # Генерируем новую карту
    def getNewMap(self):

        # Очищаем старые данные
        if self.cntr > 0:
            for ii in range(self.totalctrl.LabHeight):
                for jj in range(self.totalctrl.LabWidth):
                    self.drawLayout.removeWidget(self.ModLabs[ii][jj])
            self.ModLabs.clear()

        #Считиваем новые данные из текстовых окон и перезаписываем их, как параметры
        self.base_height = max(9,int(self.txted_1.text()))
        self.base_width = max(9,int(self.txted_2.text()))
        self.txted_1.setText(str(self.base_height))
        self.txted_2.setText(str(self.base_width))
        self.totalctrl.LabHeight = self.base_height
        self.totalctrl.LabWidth = self.base_width

        # Генерируем новые
        self.totalctrl.GeneratePrimaryLabyrint()
        self.ModLabs = [[0] * self.totalctrl.LabWidth for i in range(self.totalctrl.LabHeight)]
        self.drawPictures()
        self.cntr = 1

        return

    # Генерируем упрощенную карту
    def getNewMapSmpl(self):

        # Очищаем старые данные
        if self.cntr > 0:
            for ii in range(self.totalctrl.LabHeight):
                for jj in range(self.totalctrl.LabWidth):
                    self.drawLayout.removeWidget(self.ModLabs[ii][jj])
            self.ModLabs.clear()

        # Считиваем новые данные из текстовых окон и перезаписываем их, как параметры
        self.base_height = max(9, int(self.txted_1.text()))
        self.base_width = max(9, int(self.txted_2.text()))
        self.txted_1.setText(str(self.base_height))
        self.txted_2.setText(str(self.base_width))
        self.totalctrl.LabHeight = self.base_height
        self.totalctrl.LabWidth = self.base_width

        # Генерируем новые
        self.totalctrl.GenerateSimpleLabyrint()
        self.ModLabs = [[0] * self.totalctrl.LabWidth for i in range(self.totalctrl.LabHeight)]
        self.drawPictures()
        self.cntr = 1

        return


    # отрисовываем тайлы, соответствующие объектам
    def drawPictures(self):
        for ii in range(self.totalctrl.LabHeight):
            for jj in range(self.totalctrl.LabWidth):
                pixmap = QtGui.QPixmap(self.totalctrl.GenObjMatrix.Mtrx[ii][jj].csSprite)

                self.ModLabs[ii][jj] = ModLabel(ii*60, jj*60, self.totalctrl, self)
                self.ModLabs[ii][jj].setPixmap(pixmap)
                self.ModLabs[ii][jj].setGeometry(0, 0, 60, 60)
                self.drawLayout.addWidget(self.ModLabs[ii][jj], ii, jj)

        self.drawGroupBox.setLayout(self.drawLayout)
        self.scrlDrawArea.setWidget(self.drawGroupBox)
        return

    def partialDraw(self, ii, jj):
        pixmap = QtGui.QPixmap(self.totalctrl.GenObjMatrix.Mtrx[ii][jj].csSprite)
        self.ModLabs[ii][jj].setPixmap(pixmap)
        return


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Labyrinth Editor"))
        self.gnrtBtn.setText(_translate("MainWindow", "Generator"))
        self.saveBtn.setText(_translate("MainWindow", "Save map"))
        self.loadBtn.setText(_translate("MainWindow", "Load map"))
        self.bsgenBtn.setText(_translate("MainWindow", "Base gen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())

