import Dynamic_Object, Player_Object, Vector

class DynamicOne(Dynamic_Object.DynamicItems):
    """Наступить-одна реплика-исчезнуть"""

    def __init__(self):
        super().__init__()

    def GoThrough(self, player):
        if len(self.csMessageBox) > 0:
            player.SetMessage(self.csMessageBox[self.iCurrMessage])
            self.iCurrMessage += 1
            if self.iCurrMessage >= len(self.csMessageBox):
                    self.iCurrMessage = 0
        player.bObsDis = self.iPosition
        return True

    def ToPlayerInteract(self, player):
        return None