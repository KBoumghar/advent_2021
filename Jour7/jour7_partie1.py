import statistics as st

crabPositionList = []

with open("input.txt") as f:
    crabPositionList = f.readline().split(",")

for i in range(len(crabPositionList)):
    crabPositionList[i] = int(crabPositionList[i])

goal = int(st.median(crabPositionList))

counter = 0

for i in range(len(crabPositionList)):
    counter += abs(crabPositionList[i] - goal)

print(counter)