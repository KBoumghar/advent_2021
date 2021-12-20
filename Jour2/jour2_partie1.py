horizontalPosition = 0
verticalPosition = 0
instructionList = []
with open("input.txt") as f:
    instructionList = [line.rstrip() for line in f]

for x in instructionList:
    if "forward" in x:
        horizontalPosition += int(x[len(x)-1])
    elif "down" in x:
        verticalPosition += int(x[len(x)-1])
    else:
        verticalPosition -= int(x[len(x)-1])

print(verticalPosition*horizontalPosition)