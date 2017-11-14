import Game_Object, World_Object, Vector

class Player(Game_Object.GameObject):
    """Класс игрока"""

    def __init__(self):
        super().__init__()
        self.iHealth = 10
        self.csSprite = "Player.gif"
        self.iDestination = Vector.Vector()
        self.csPlayerMessage = []
        self.bObsDis = None # Признак того, что объект с которым провзаимодейстовали/прошли нужно убрать

    # УСТАНОВКА ПАРАМЕТРОВ ИГРОКА
    # Изменяем текущий уровень жизней
    def ChangeLife(self, iAddition):
        self.iHealth += iAddition

        return

    # Проверяем текущее состояние
    def CheckState(self):
        if self.iHealth <= 0:
            return "Death"
        if self.iPosition == self.iDestination:
            return "Win"

    # ВЗАИМОДЕЙСТВИЕ С ОКРУЖАЮЩИМ ИГРОВЫМ МИРОМ
    # Взять предмет игрового мира
    def TakeItem(self, gitem):
        self.lstStash.append(gitem)

        return

    # Отдать предмет из инвентаря
    def GiveItem(self, csItemName):
        # Проверяем, что такая вещь в инвентаре
        chk = 0
        for itm in self.lstStash:
            if csItemName == itm.GetName():
                break
            chk += 1

        if chk == len(self.lstStash):
            return None
        else:
            return self.lstStash.pop(chk)

    # Осматриваем объект игрового мира
    def WatchOut(self, gitem):
        ans = gitem.GetDescription()

        return ans

    # Взаимодействуем с объектом игрового мира
    def Interact(self, gitem): # Взаимодействие с объектами игрового мира
        ans = gitem.ToPlayerInteract(self)
        if ans == "Dissapear":
            #self.bObsDis = True
            self.bObsDis = gitem.iPosition
        else:
            SetMessage(ans)
        return ans

    # Проверка прохождения через объект игрового мира
    def GoThrough(self, gitem):
        ans = gitem.GoThrough(self)

        return ans

    # Подсветить область вокруг игрока
    def EnlightMe(self, radii):
        # В ходе рисования видимой области вокруг игрока, подумаем, что функция должна возвращать
        # Скорее всего, это будут координаты игрока и радиус подсветки
        iData = [self.iPosition, radii]
        return iData

    # Получить сообщение от объекта игрового мира
    def SetMessage(self, csMsg):
        self.csPlayerMessage = [csMsg]

        return

    def GetMessage(self):
        return self.csPlayerMessage