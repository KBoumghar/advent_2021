inputList = []
number1 = 0
number2 = 0
with open("input.txt") as f:
    inputList = [line.rstrip() for line in f]

oxygenRating = inputList
scrubberRating = inputList.copy()

def oneMajority(bitList, i):
    oneCounter = 0
    for x in bitList:
        if x[i] == "1":
            oneCounter += 1

    if oneCounter >= len(bitList) / 2.0:
        return True
    return False

i = 0
while True:
    j = 0
    counter = 0
    size = len(oxygenRating)
    if oneMajority(oxygenRating, i):
        while j < len(oxygenRating):
            str = oxygenRating[j]
            if str[i] == "0":
                oxygenRating.pop(j)
                j -= 1
            j += 1
    else:
        while j < len(oxygenRating):
            str = oxygenRating[j]
            if str[i] == "1":
                oxygenRating.pop(j)
                j -= 1
            j += 1
    i += 1
    if len(oxygenRating) == 1:
        break


i = 0
while True:
    j = 0
    counter = 0
    size = len(scrubberRating)
    if oneMajority(scrubberRating, i):
        while j < len(scrubberRating):
            str = scrubberRating[j]
            if str[i] == "1":
                scrubberRating.pop(j)
                j -= 1
            j += 1
    else:
        while j < len(scrubberRating):
            str = scrubberRating[j]
            if str[i] == "0":
                scrubberRating.pop(j)
                j -= 1
            j += 1
    i += 1
    if len(scrubberRating) == 1:
        break

oxygenRate = oxygenRating[0]
scrubberRate = scrubberRating[0]

for i in range(len(oxygenRate)):
    number1 += 2**i * int(oxygenRate[len(oxygenRate) - (i+1)])
    number2 += 2**i * int(scrubberRate[len(scrubberRate) - (i+1)])

print(number1 * number2)