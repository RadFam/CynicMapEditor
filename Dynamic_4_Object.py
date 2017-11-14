import Dynamic_Object, Player_Object, Static_Object, Vector

class DynamicFour(Dynamic_Object.DynamicItems):
    """Взаимодейстововать-цепь действий-не исчезать"""

    def __init__(self):
        super().__init__()
        self.lstProcessArray = [] # [Replica_1, take item, give item, replica_2]
        self.iProcessStage = 0

    def AddProcess(self, proc):
        self.lstProcessArray.append(proc)

        return

    def AddToStash(self, gitem):
        self.lstStash.append(gitem)

        return

    def TakeFromStash(self, csItemName):
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

###################################################################################
    def GoThrough(self, player):
        player.bObsDis = None
        return self.bCanPas

    def ToPlayerInteract(self, player):
        # В основном, взаимодействие будет сводиться к обмену вещей
        if self.iProcessStage < len(self.lstProcessArray):
            # Проверяем, есть ли у игрока то, что нам нужно
            csRetMsg = [self.lstProcessArray[self.iProcessStage][0]]
            itm = player.GiveItem(self.lstProcessArray[self.iProcessStage][1])
            # Игрок принес то, что нам нужно
            if itm is not None:
                csRetMsg.append(self.lstProcessArray[self.iProcessStage][3])
                self.AddToStash(itm)

                csNm = self.lstProcessArray[self.iProcessStage][2]
                # Находим его у себя в инвентаре и отдаем
                itm2 = self.TakeFromStash(csNm)
                player.TakeItem(itm2)

                self.iProcessStage += 1

            return csRetMsg