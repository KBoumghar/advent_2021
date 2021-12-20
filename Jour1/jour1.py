import numpy as np
import os

previous = float('inf')
counter = 0
numberList = []
with open("input.txt") as f:
    numberList = [line.rstrip() for line in f]

for x in numberList:
    if int(x) > previous:
        counter += 1
    previous = int(x)

print(counter)
