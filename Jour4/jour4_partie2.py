import copy

numberDrawList = []
bingoCardList = []
bingoCardMap = []
vectorList = [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]
#2-6
#8-12
with open("input.txt") as f:
    lines = f.readlines()
    numberDrawList = lines[0].rstrip().split(",")
    counter = 0
    i = 0
    for counter in range(100):
        i = 6*counter + 2
        bingoCard = []
        for k in range(5):
            bingoCard.append(lines[i+k].strip().split())
        bingoCardList.append(bingoCard)
        counter += 1

for i in range(len(bingoCardList)):
    bingoCardMap.append(copy.deepcopy(vectorList))


def bingoCheck(bingoMap):
    return rowCheck(bingoMap) or columnCheck(bingoMap)


def rowCheck(bingoMap):
    for i in range (len(bingoMap)):
        if all(bingoMap[i]):
            return True
    return False


def columnCheck(bingoMap):
    size = len(bingoMap)
    for i in range(size):
        counter = 0
        for j in range(size):
            if bingoMap[j][i]:
                counter += 1
            else:
                break
        if counter == size:
            return True
    return False


def cardCheck(bingoCard, bingoMap, number):
    size = len(bingoCard)
    for i in range(size):
        for j in range(size):
            if number == bingoCard[i][j]:
                bingoMap[i][j] = True
                return True
    return False


def bingoSum(bingoCard, bingoMap, number):
    size = len(bingoCard)
    sum = 0

    for i in range(size):
        for j in range(size):
            if not bingoMap[i][j]:
                sum += int(bingoCard[i][j])

    return sum * int(number)


numberSet = set()
size = len(bingoCardList)
winningBoard = size + 1
stop = False
for number in numberDrawList:
    for k in range(size):
        if len(numberSet) == size - 1 and not stop:
            stop = True
            for i in range(size):
                if i not in numberSet:
                    winningBoard = i
        if cardCheck(bingoCardList[k], bingoCardMap[k], number):
            if bingoCheck(bingoCardMap[k]):
                numberSet.add(k)
                if k == winningBoard:
                    print(bingoSum(bingoCardList[winningBoard], bingoCardMap[winningBoard], number))





