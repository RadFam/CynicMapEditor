import Labyrint
import random

# 1 - стена
# 2 - проход

class  PrimmLabyrint(Labyrint.Labyrint):
    """Заполнение лабиринта по алгоритму Прима"""

    def GenerateMaze(self, iWidth, iHeight):
        self.iWidth = iWidth
        self.iHeight = iHeight

        #self.bUserMaze = ([[0, 1] * ((self.iWidth - 1) // 2) + [0]] + [[1] * self.iWidth]) * ((self.iHeight - 1) // 2) + [[0, 1] * ((self.iWidth - 1) // 2) + [0]]
        #self.bInnerMaze = ([["", 1] * ((self.iWidth - 1) // 2) + [""]] + [[1] * self.iWidth]) * ((self.iHeight - 1) // 2) + [["", 1] * ((self.iWidth - 1) // 2) + [""]]
        for ii in range(self.iHeight):
            if ii % 2 == 0:
                self.bUserMaze.append([0, 1] * ((self.iWidth - 1) // 2) + [0])
                self.bInnerMaze.append(["", 1] * ((self.iWidth - 1) // 2) + [""])
            elif ii % 2 == 1:
                self.bUserMaze.append([1] * self.iWidth)
                self.bInnerMaze.append([1] * self.iWidth)

        iCntr = 1
        self.bUserMaze[self.iStY][self.iStX] = 2 # Поле уже помечено

        while iCntr < ((self.iWidth + 1) // 2)*((self.iHeight + 1) // 2):

            iNextStep = [(self.iStX, self.iStY-2, "N"), (self.iStX+2, self.iStY, "E"), (self.iStX, self.iStY+2, "S"), (self.iStX-2, self.iStY, "W")] # North, East, South, West
            random.shuffle(iNextStep)

            chk = 0
            for (xx , yy, strSide) in iNextStep:
                if not (0 <= xx <= self.iWidth-1 and 0 <= yy <= self.iHeight - 1):
                    continue
                elif (0 <= xx <= self.iWidth-1 and 0 <= yy <= self.iHeight - 1) and (self.bUserMaze[yy][xx] == 2):
                    continue
                elif (0 <= xx <= self.iWidth-1 and 0 <= yy <= self.iHeight - 1) and (self.bUserMaze[yy][xx] == 0):
                    chk = 1
                    self.bUserMaze[yy][xx] = 2
                    self.bInnerMaze[yy][xx] = strSide
                    if strSide == "N":
                        self.bUserMaze[self.iStY-1][self.iStX] = 2
                    elif strSide == "E":
                        self.bUserMaze[self.iStY][self.iStX+1] = 2
                    elif strSide == "S":
                        self.bUserMaze[self.iStY+1][self.iStX] = 2
                    elif strSide == "W":
                        self.bUserMaze[self.iStY][self.iStX-1] = 2
                    self.iStX = xx
                    self.iStY = yy
                    iCntr += 1
                    break

            if chk == 0: # ничего не смогли выбрать, следовательно, откатываемся на клетку назад
                strSide = self.bInnerMaze[self.iStY][self.iStX]
                if strSide == "N":
                    self.iStY += 2
                elif strSide == "E":
                    self.iStX -= 2
                elif strSide == "S":
                    self.iStY -= 2
                elif strSide == "W":
                    self.iStX += 2
                elif strSide == "":
                    break

        # print(self.bUserMaze)
        return self.bUserMaze
        #print(self.bInnerMaze)
        #self.FinalizeMaze()