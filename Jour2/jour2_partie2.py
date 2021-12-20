horizontalPosition = 0
verticalPosition = 0
aim = 0
instructionList = []
with open("input.txt") as f:
    instructionList = [line.rstrip() for line in f]

for x in instructionList:
    if "forward" in x:
        increase = int(x[len(x)-1])
        horizontalPosition += increase
        verticalPosition += increase * aim
    elif "down" in x:
        aim += int(x[len(x)-1])
    else:
        aim -= int(x[len(x)-1])

print(verticalPosition*horizontalPosition)