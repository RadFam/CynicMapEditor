import Game_Object, Player_Object, Vector

class WorldObject(Game_Object.GameObject):
    """Просто отделим игровые объекты от общего абстрактного класса"""

    def __init__(self):
        super().__init__()

        self.csSprite = ""
        self.bCanPas = True

    def ToPlayerInteract(self, player):
        pass

    def SetSprite(self, csSprt):
        self.csSprite = csSprt

        return

    def SetPass(self, bCP):
        self.bCanPass = bCP

        return

    def GoThrough(self, player):
        pass

    def Dissapear(self):
        return "Dissapear"