from ObjectMatrix import ObjectMatrix
from PrimmLabyrint import PrimmLabyrint
from Comm import Communicate

from Dynamic_1_Object import DynamicOne
from Dynamic_2_Object import DynamicTwo
from Dynamic_3_Object import DynamicThree
from Dynamic_4_Object import DynamicFour
from Dynamic_5_Object import DynamicFive
from Static_Object import StaticItems

import Dyn_5_widget
import Dyn_4_widget
import Dyn_13_widget

import pickle

# Нам нужно загрузить файл со списком объектов!

class TCL(object):

    def __init__(self, mainDlg):
        self.LabWidth = 31
        self.LabHeight = 31
        self.GenObjMatrix = ObjectMatrix(self.LabWidth, self.LabHeight)

        self.s_01 = Communicate()
        self.s_01.lbClickData_dlg_ret.connect(mainDlg.partialDraw)
        self.mndlg = mainDlg

        # загрузим список базовых объектов игрового мира
        with open('ObjectCollection_3.pckl', 'rb') as f:
            self.ObjectList = pickle.load(f)

    # Сгенерировать сложный лабиринт
    def GeneratePrimaryLabyrint(self):
        Lab = PrimmLabyrint()
        Tmp = Lab.GenerateMaze(self.LabWidth, self.LabHeight)
        self.GenObjMatrix = []
        self.GenObjMatrix = ObjectMatrix(self.LabHeight, self.LabWidth)
        for ii in range(self.LabHeight):
            for jj in range(self.LabWidth):
                if Tmp[ii][jj] == 1:
                    self.GenObjMatrix.Mtrx[ii][jj] = self.ObjectList[1]
                if Tmp[ii][jj] == 2:
                    self.GenObjMatrix.Mtrx[ii][jj] = self.ObjectList[2]

        return

    # Сгенерировать простой лабиринт
    def GenerateSimpleLabyrint(self):
        self.GenObjMatrix = []
        self.GenObjMatrix = ObjectMatrix(self.LabHeight, self.LabWidth)
        for ii in range(self.LabHeight):
            for jj in range(self.LabWidth):
                self.GenObjMatrix.Mtrx[ii][jj] = self.ObjectList[2]

        return

    # Заменить элемент игрового поля
    def changeElement(self, ii, jj, oNum):
        self.GenObjMatrix.Mtrx[ii][jj] = self.ObjectList[oNum]
        self.s_01.lbClickData_dlg_ret.emit(ii, jj)
        return

    # Изменить элемент игрового поля
    def modifyElement(self, ii, jj):
        # Определим тип объекта, который находится по данному адресу
        fullTypeName = str(type(self.GenObjMatrix.Mtrx[ii][jj]))
        shortTypeName = fullTypeName[fullTypeName.find('.')+1:len(fullTypeName)-2]

        # Вызываем соответсвующие диалоговые окошки
        if shortTypeName in ['DynamicOne', 'DynamicTwo', 'DynamicThree']:
            newWind = Dyn_13_widget.Ui_Dyn13_widget(ii, jj, self, self.mndlg)
            newWind.show()

        if shortTypeName == 'DynamicFour':
            newWind = Dyn_4_widget.Ui_Dyn4_widget(ii, jj, self, self.mndlg)
            newWind.show()

        if shortTypeName == 'DynamicFive':
            newWind = Dyn_5_widget.Ui_Dyn5_widget(ii, jj, self, self.mndlg)
            newWind.show()
            #print("Widget is closed")

        return

    def updateDynamicFive(self, str_1, str_2, item, yPos, xPos):
        # Изменим атрибуты ссответствующего объекта
        print(str_1, str_2, item, yPos, xPos)
        self.GenObjMatrix.Mtrx[yPos][xPos].lstProcess = [str_1, item, str_2]
        return

    def updateDynamicFour(self, str_1, str_2, item_t, item_g, yPos, xPos):
        # Изменим атрибуты ссответствующего объекта
        print(str_1, str_2, item_t, item_g, yPos, xPos)
        self.GenObjMatrix.Mtrx[yPos][xPos].lstProcessArray.append([str_1, item_t, item_g, str_2])
        aaa = 0
        return

    def updateDynamicOneThree(self, str, yPos, xPos):
        print(str, yPos, xPos)
        self.GenObjMatrix.Mtrx[yPos][xPos].csMessageBox = [str]
        return

    # Сохранение данных
    def SaveObjMatrix(self, filename):
        ToSaveStruct = []
        ToSaveStruct.append(self.LabHeight)
        ToSaveStruct.append(self.LabWidth)
        for ii in range(self.LabHeight):
            for jj in range(self.LabWidth):
                ToSaveStruct.append(self.GenObjMatrix.Mtrx[ii][jj])
        # Теперь через pickle записываем данные
        with open(filename, "wb") as f:
            pickle.dump(ToSaveStruct, f)

        return

    # Загрузка данных
    def LoadObjMatrix(self, filename):
        TmpStruct = []
        with open(filename, 'rb') as f:
            TmpStruct = pickle.load(f)

        # Затираем предыдущую структуру (если она, конечно же есть)
        cnt = 2
        self.LabHeight = TmpStruct[0]
        self.LabWidth = TmpStruct[1]
        self.GenObjMatrix = []
        self.GenObjMatrix = ObjectMatrix(self.LabHeight, self.LabWidth)
        for ii in range(self.LabHeight):
            for jj in range(self.LabWidth):
                self.GenObjMatrix.Mtrx[ii][jj] = TmpStruct[cnt]
                cnt += 1

        #self.mndlg.drawPictures();
        return