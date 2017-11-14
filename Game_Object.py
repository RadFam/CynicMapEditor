import Vector

class GameObject(object):
    """Базовый абстрактный класс для всех игровых объектов"""

    def __init__(self):
        self.iPosition = Vector.Vector() # Координаты на игровом поле (в клетку)
        self.lstStash = [] # "Рюкзак" - мето хранения других объектов
        self.csDescription = ""
        self.csName = ""

    def SetDescription(self, csDscr):
        self.csDescription = csDscr

        return

    def SetName(self, csNm):
        self.csName = csNm

        return

    def SetPosition(self, iPos):
        self.iPosition.x, self.iPosition.y = iPos.x, iPos.y

    def GetDescription(self):
        return self.csDescription

    def GetName(self):
        return self.csName

    #def GoThrough(self):
        #pass