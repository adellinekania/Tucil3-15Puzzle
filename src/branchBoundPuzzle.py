from colorama import Fore

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

def markSolution(isSolution, tree):
    # print("AMAN GA")
    # printTreeData(tree.data)
    if tree.parent != None :
        tree.isSolution = isSolution
        markSolution(isSolution, tree.parent)

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

def printTreeData(data):
    for x in data:
        print(x)

# Menampilkan data dari sebuah tree
def printTreeSolution(tree):
    if (tree.parent != None):
        print(f"{Fore.LIGHTCYAN_EX}Pergeseran tile kosong: {Fore.LIGHTYELLOW_EX}{tree.direction}{Fore.WHITE}")
        printTreeData(tree.data)
        print("\n")

    isFound = False
    i = 0
    if len(tree.child) > 0:
        while i < len(tree.child) and not isFound:
            if tree.child[i].isSolution:
                isFound = True
                child = tree.child[i]
            else:
                i += 1
        printTreeSolution(child)



# Fungsi rekrusif untuk menentukan solusi dari 15 Puzzle
def solve15Puzzle(currentTree, rootTree, queueTree, solutionTree, count):
    # Menentukan semua kemungkinan child dari currenTree
    currentTree.getChild(count)

    # Menentukan nilai tree dengan cost minimum yang masih hidup
    # pada child dan queue
    minGTree = currentTree.child[0].countC
    minTree = currentTree.child[0]
    isOnQueue = False
    indexOnQueue = 0
    
    for tree in currentTree.child:
        if tree.countC < minGTree:
            minTree = tree
            minGTree = tree.countC

    while not isOnQueue and indexOnQueue < len(queueTree):
        if queueTree[indexOnQueue].countC < minGTree:
            minTree = queueTree[indexOnQueue]
            minGTree = queueTree[indexOnQueue].countC
            isOnQueue = True
        else:
            indexOnQueue += 1

    # Menghapus tree yang merupakan tree dengan cost minimum apabila
    # tree tersebut terdapat pada queue
    if isOnQueue:
        del queueTree[indexOnQueue]
        markSolution(False, currentTree)
        markSolution(True, minTree)
    else:
        minTree.isSolution = True

    # Menambahkan child dari currentTree yang bukan tree dengan
    # cost minimum pada queueTree
    for tree in currentTree.child:
        if tree != minTree:
            queueTree.append(tree)

    # Apabila belum mencapai solusi, akan memanggil fungsi
    # solve15Puzzle secara rekrusif
    if (minTree.countC - minTree.count > 0):
        solve15Puzzle(minTree, rootTree, queueTree, solutionTree, count+1)
    else:
        printTreeSolution(rootTree)