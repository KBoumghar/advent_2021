inputList = []
gammaRate = ""
epsilonRate = ""
number1 = 0
number2 = 0
bitArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
with open("input.txt") as f:
    inputList = [line.rstrip() for line in f]

for x in inputList:
    for i in range(len(x)):
        if x[i] == "1":
            bitArray[i] += 1

size = len(inputList)
for i in range(len(bitArray)):
    if bitArray[i] >= size/2.0:
        gammaRate = gammaRate + "1"
        epsilonRate = epsilonRate + "0"
    else:
        gammaRate = gammaRate + "0"
        epsilonRate = epsilonRate + "1"

for i in range(len(gammaRate)):
    number1 += 2**i * int(gammaRate[len(gammaRate) - (i+1)])
    number2 += 2**i * int(epsilonRate[len(epsilonRate) - (i+1)])

print(number1 * number2)