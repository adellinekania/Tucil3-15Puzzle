from random import randrange

def read15PuzzleFromFile(filepath):
    f = open(filepath, "r")
    data = []
    for i in range(0,4):
        str = f.readline()
        if i != 3 :
            data.append(str[0:-1].split())
        else:
            data.append(str.split())
    for i in range(0,4):
        for j in range(0,4):
            data[i][j] = int(data[i][j])
    return data

def createRandomPuzzle():
    data = []
    arrData = []
    possibleInt = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    i = 15
    while i >= 0:
        if i > 0:
            idx = randrange(i)
        else:
            idx = 0
        arrData.append(possibleInt[idx])
        if i % 4 == 0:
            data.append(arrData)
            arrData = []
        del possibleInt[idx]
        i -= 1
    return data