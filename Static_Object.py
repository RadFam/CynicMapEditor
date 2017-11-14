import World_Object, Player_Object, Vector

class StaticItems(World_Object.WorldObject):

    def __init__(self):
        super().__init__()
        self.bCanCollect = True

    def SetCollect(self, bCC):
        self.bCanCollect = bCC

        return

    def GoThrough(self, player):
        player.bObsDis = None
        return self.bCanPas

    def ToPlayerInteract(self, player):

        # Если это не лечилка
        if self.bCanCollect and self.csName != "Heal":
            player.TakeItem(self)
            player.bObsDis = self.iPosition
            #return self.Dissapear()
            return "Dissapear"

        # Если это лечилка
        elif self.bCanCollect and self.csName == "Heal":
            player.ChangeLife(1)
            player.bObsDis = self.iPosition
            #return self.Dissapear()
            return "Dissapear"

        # Если это вспышка света
        elif self.csName == "Flash":
            player.EnlightMe(3)
            player.bObsDis = self.iPosition
            #return self.Dissapear()
            return "Dissapear"

        else:
            return "None"