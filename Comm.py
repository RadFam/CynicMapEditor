from PyQt5.QtCore import pyqtSignal, QObject


class Communicate(QObject):

    lbClickData_lbl = pyqtSignal(int, int)  #  сигнал от лейбла о нажатии левой кнопки
    rbClickData_lbl = pyqtSignal(int, int)  #  сигнал от лейбла о нажатии правой кнопки
    lbClickData_dlg = pyqtSignal(int, int, int)  #  сигнал от окна редактора о нажатии левой кнопки
    rbClickData_dlg = pyqtSignal(int, int)  #  сигнал от окна редактора о нажатии правой кнопки
    lbClickData_dlg_ret = pyqtSignal(int, int)  #  ответ от класса управления на нажатие левой кнопки

    dyn5_SendData = pyqtSignal(str, str, str, int, int)
    dyn4_SendData = pyqtSignal(str, str, str, str, int, int)
    dyn13_SendData = pyqtSignal(str, int, int)

    saveFile = pyqtSignal(str) # сигнал о том, что надо сохранить данные
    loadFile = pyqtSignal(str)  # сигнал о том, что надо загрузить данные