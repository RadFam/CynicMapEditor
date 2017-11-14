class ObjectMatrix(object):

    def __init__(self, a, b):
        self.rows = a
        self.columns = b
        self.Mtrx = [[0] * self.columns for i in range(self.rows)]

    def ChangeSize(self,a , b):
        self.Mtrx = None
        self.rows = a
        self.columns = b
        self.Mtrx = [[0] * self.columns for i in range(self.rows)]
        #self.Mtrx = [[] * self.columns] * self.rows
        return
