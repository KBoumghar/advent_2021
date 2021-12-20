previous = float('inf')
counter = 0
numberList = []

with open("input.txt") as f:
    numberList = [line.rstrip() for line in f]

for i in range(len(numberList) - 2):
    sum = int(numberList[i]) + int(numberList[i+1]) + int(numberList[i+2])
    if (sum > previous):
        counter += 1
    previous = sum

print(counter)