from colorama import Fore

# Kelas yang menyimpan simpul-simpul yang merupakan solusi dalam bentuk
# struktur data pohon
class TreeSolution:
    def __init__(self, data, parent, child, direction):
        self.data = data
        self.parent = parent
        self.child = child
        self.direction = direction

# Fungsi untuk menentukan nilai Kurang dari suatu 15 puzzle untuk
# menentukan apakah 15 puzzle tersebut dapat diselesaikan atau tidak
def findKurang(data):
    sumKurang = 0
    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(i, 4):
                for l in range(0, 4):
                    if((k == i and l > j) or k > i):
                        if(data[k][l] < data[i][j]):
                            sumKurang += 1
            if((i + j) % 2 == 1 and data[i][j] == 16):
                sumKurang += 1
    return sumKurang

# Menentukan nilai fungsi g dari suatu matrix 15 puzzle
def findGFunction(data):
    count = 1
    g = 0
    for i in range(0,4):
        for j in range(0,4):
            if (count != data[i][j]):
                g += 1
            count += 1
    return g

# Membuat pohon solusi dari node simpul yang merupakan solusi
def createTreeSolution(tree, treeSolution):
    if tree.parent != None:
        parentTree = tree.parent
        parentTreeSolution = TreeSolution(parentTree.data, None, treeSolution, parentTree.direction)
        createTreeSolution(parentTree, parentTreeSolution)
    else:
        printTreeSolution(treeSolution)

# Menampilkan data dari sebuah tree
def printTreeSolution(tree):
    if (tree != None and tree.child != None):
        tree = tree.child
        print(f"{Fore.LIGHTCYAN_EX}Pergeseran tile kosong: {Fore.LIGHTYELLOW_EX}{tree.direction}{Fore.WHITE}")
        printTreeData(tree.data)
        print("\n")
        printTreeSolution(tree)

# Menampilkan data 
def printTreeData(data):
    for x in data:
        print(x)


# Fungsi untuk menentukan solusi dari 15 Puzzle
def solve15Puzzle(queueTree):
    # Variabel untuk menghitung urutan matriks
    # dan menandakan pencarian solusi ditemukan
    count = 0
    isSolved = False

    # Dictionary untuk menyimpan matriks/data yang sudah pernah dicoba
    # agar tidak dicoba lagi
    visitedData = dict()

    while not isSolved and not queueTree.empty():
        isUnique = False

        # Mencari simpul dengan cost minimum dari queue
        while not isUnique and not queueTree.empty():
            minTree = queueTree.get()[2]

            # Apabila ternyata matriks/data simpul sudah pernah ditelusuri,
            # akan mencari lagi matriks yang belum ditelusuri
            if visitedData.get(str(minTree.data)) == None:
                visitedData[str(minTree.data)] = 1
                isUnique = True
        
        # Apabila queueTree kosong, dan tidak ditemukan minTree
        if not isUnique:
            print("Solusi tidak bisa ditemukan")
            return

        # Apabila simpul merupakan solusi
        if(minTree.countC - minTree.count == 0):
            isSolved = True
            treeSolution = TreeSolution(minTree.data, None, None, minTree.direction)
            createTreeSolution(minTree, treeSolution)
            return

        # Jika simpul bukan merupakan solusi, akan mencari semua kemungkinan
        # anak dari simpul tersebut dan memasukkanya ke dalam queue
        minTree.getChild(minTree.count + 1)

        for child in minTree.child:
            count += 1
            queueTree.put((child.countC, count, child))
    
    if not isSolved:
        print("Solusi tidak bisa ditemukan")
        return