import Dynamic_Object, Player_Object, Static_Object, Vector

class DynamicFive(Dynamic_Object.DynamicItems):
    """Взаимодейстововать-произвести действие-исчезнуть"""

    def __init__(self):
        super().__init__()
        self.lstProcess = [] # [Replica_1, Take item, Replica_2]
        self.iProcessStage = 0

    def AddProcess(self, proc):
        self.lstProcess.append(proc)

        return

    def AddToStash(self, gitem):
        self.lstStash.append(gitem)

        return

    def GoThrough(self, player):
        player.bObsDis = None
        return self.bCanPas

    def ToPlayerInteract(self, player):
        # В основном, взаимодействие будет сводиться к приему определенной вещи
        if self.iProcessStage < len(self.lstProcessArray):

            # Проверяем, есть ли у игрока то, что нам нужно
            csRetMsg = [self.lstProcessArray[self.iProcessStage][0]]
            itm = player.GiveItem(self.lstProcessArray[self.iProcessStage][1])
            # Игрок принес то, что нам нужно
            if itm is not None:
                csRetMsg.append(self.lstProcessArray[self.iProcessStage][3])
                self.AddToStash(itm)

                self.iProcessStage += 1

                # А теперь исчезнем
                player.bObsDis = self.iPosition

            return csRetMsg