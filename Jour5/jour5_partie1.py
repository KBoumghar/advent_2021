maxValue = 1000
listOfZero = [0] * maxValue
pointList = []
inputList = []
with open("input.txt") as f:
    inputList = f.read().splitlines()

for i in range(maxValue):
    pointList.append(listOfZero.copy())

for i in range(len(inputList)):
    line = inputList[i].split(" -> ")
    point1 = line[0].split(",")
    point2= line[1].split(",")
    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])

    if x1 == x2:
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp

        iter = y1
        while iter <= y2:
            pointList[x1][iter] += 1
            iter +=1

    elif y1 == y2:
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp

        iter = x1
        while iter <= x2:
            pointList[iter][y1] += 1

            iter += 1

counter = 0

for i in range(maxValue):
    for j in range(maxValue):
        if pointList[i][j] >= 2:
            counter += 1

print(counter)

