fishList = []
dayLimit = 8
numberOfDay = 256
listOfEight = [8]
with open("input.txt") as f:
    fishList = f.readline().split(",")


listCounter = [0] * (dayLimit+1)
for i in range (len(fishList)):
    if fishList[i] == "1":
        listCounter[1] += 1
    elif fishList[i] == "2":
        listCounter[2] += 1
    elif fishList[i] == "3":
        listCounter[3] += 1
    elif fishList[i] == "4":
        listCounter[4] += 1
    elif fishList[i] == "5":
        listCounter[5] += 1


for i in range (numberOfDay):
    temp = listCounter[0]
    for j in range(len(listCounter)-1):
        listCounter[j] = listCounter[j+1]
    listCounter[6] += temp
    listCounter[8] = temp

print(sum(listCounter))
