class Labyrint(object):
    """Определение базового абстрактного класса Лабиринт"""

    def __init__(self):
        self.iWidth = 0 # Всегда нечетное число
        self.iHeight = 0 # Всегда нечетное число
        self.iStX = 0
        self.iStY = 0
        self.bUserMaze = [] # iWidth*iHeight
        self.bInnerMaze = [] # ((iWidth-1)/2)*((iHeight-1)/2)

    def FinalizeMaze(self):

        for yy in range(self.iHeight - 2):
            for xx in range(self.iWidth - 2):
                if self.bUserMaze[yy][xx] == 2 and self.bUserMaze[yy][xx+2] == 2:
                    self.bUserMaze[yy][xx+1] = 2
                elif self.bUserMaze[yy][xx] == 2 and self.bUserMaze[yy+2][xx] == 2:
                    self.bUserMaze[yy+1][xx] = 2
                elif self.bUserMaze[yy][xx+2] == 2 and self.bUserMaze[yy+2][xx+2] == 2:
                    self.bUserMaze[yy+1][xx+2] = 2
                elif self.bUserMaze[yy+2][xx] == 2 and self.bUserMaze[yy+2][xx+2] == 2:
                    self.bUserMaze[yy+2][xx+1] = 2

        print(self.bUserMaze)
        return


    #def GenerateMaze(self, iWidth, iHeight):
    #    pass