import statistics as st

crabPositionList = []

with open("input.txt") as f:
    crabPositionList = f.readline().split(",")

for i in range(len(crabPositionList)):
    crabPositionList[i] = int(crabPositionList[i])

goal = int(st.mean(crabPositionList))
goal2 = int(st.mean(crabPositionList)) + 1

counter = 0

for i in range(len(crabPositionList)):

    diff = abs(crabPositionList[i] - goal)
    counter += (diff+1)*diff/2

print(counter)