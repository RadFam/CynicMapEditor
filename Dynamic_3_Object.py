import Dynamic_Object, Player_Object, Vector

class DynamicThree(Dynamic_Object.DynamicItems):
    """Взаимодейстововать-одна реплика-не исчезать"""

    def __init__(self):
        super().__init__()

    def GoThrough(self, player):
        player.bObsDis = None
        return self.bCanPas

    def ToPlayerInteract(self, player):
        if len(self.csMessageBox) > 0:
            player.SetMessage(self.csMessageBox[self.iCurrMessage])
            self.iCurrMessage += 1
            if self.iCurrMessage >= len(self.csMessageBox):
                self.iCurrMessage = 0

        return "Ok"