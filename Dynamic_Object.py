import World_Object, Vector

class DynamicItems(World_Object.WorldObject):
    """Динамические объекты, с которыми игрок взаимодействет, т.е. разговаривает и отдает вещи из инвентаря"""

    def __init__(self):
        super().__init__()
        self.csMessageBox = []
        self.iCurrMessage = 0
        self.bCanCollect = True # В смысле, что объект в какой-то момент может исчезнуть

    def GoThrough(self, player):
        pass

    def ToPlayerInteract(self, player):
        pass