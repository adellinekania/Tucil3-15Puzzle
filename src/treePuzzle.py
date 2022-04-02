from branchBoundPuzzle import findGFunction
from copy import deepcopy

# Struktur data untuk menyimpan puzzle tree yang terbentuk
class Tree:
    def __init__(self, data, parent, count, direction):
        self.parent = parent
        self.child = []
        self.data = data
        self.countC = findGFunction(data) + count
        self.count = count
        self.direction = direction
        self.isSolution = False

        # Menentukan posisi tile bernomor 16
        for i in range(0,4):
            for j in range(0,4):
                if self.data[i][j] == 16:
                    self.i = i
                    self.j = j
                    return

    # Method untuk mendapatkan semua kemungkinan child berdasarkan parentnya    
    def getChild(self, count):
        # Apabila tree merupakan root
        if (self.parent == None):
            if (self.i > 0):
                moveUpData = deepcopy(self.data)
                moveUpData[self.i][self.j] = moveUpData[self.i - 1][self.j]
                moveUpData[self.i - 1][self.j] = 16
                self.child.append(Tree(moveUpData, self, count, "up"))
            if (self.i < 3):
                moveDownData = deepcopy(self.data)
                moveDownData[self.i][self.j] = moveDownData[self.i + 1][self.j]
                moveDownData[self.i + 1][self.j] = 16
                self.child.append(Tree(moveDownData, self, count, "down"))
            if (self.j > 0):
                moveLeftData = deepcopy(self.data)
                moveLeftData[self.i][self.j] = moveLeftData[self.i][self.j - 1]
                moveLeftData[self.i][self.j - 1] = 16
                self.child.append(Tree(moveLeftData, self, count, "left"))
            if (self.j < 3):
                moveRightData = deepcopy(self.data)
                moveRightData[self.i][self.j] = moveRightData[self.i][self.j + 1]
                moveRightData[self.i][self.j + 1] = 16
                self.child.append(Tree(moveRightData, self, count, "right"))

        # Apabila tree bukan root, maka pergerakan childnya tidak boleh tepat berlawanan dengan
        # arah pergerakan parent karena dapat menyebabkan posisi puzzle tidak berubah kemana-mana
        else :
            if (self.i > 0 and self.direction != "down"):
                moveUpData = deepcopy(self.data)
                moveUpData[self.i][self.j] = moveUpData[self.i - 1][self.j]
                moveUpData[self.i - 1][self.j] = 16
                self.child.append(Tree(moveUpData, self, count, "up"))
            if (self.i < 3 and self.direction != "up"):
                moveDownData = deepcopy(self.data)
                moveDownData[self.i][self.j] = moveDownData[self.i + 1][self.j]
                moveDownData[self.i + 1][self.j] = 16
                self.child.append(Tree(moveDownData, self, count, "down"))
            if (self.j > 0 and self.direction != "right"):
                moveLeftData = deepcopy(self.data)
                moveLeftData[self.i][self.j] = moveLeftData[self.i][self.j - 1]
                moveLeftData[self.i][self.j - 1] = 16
                self.child.append(Tree(moveLeftData, self, count, "left"))
            if (self.j < 3 and self.direction != "left"):
                moveRightData = deepcopy(self.data)
                moveRightData[self.i][self.j] = moveRightData[self.i][self.j + 1]
                moveRightData[self.i][self.j + 1] = 16
                self.child.append(Tree(moveRightData, self, count, "right"))