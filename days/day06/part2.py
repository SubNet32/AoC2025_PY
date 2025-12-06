import time
from functools import reduce
from operator import mul
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()


values = [[x, []] for x in file.pop().split() if x != ""]

blockIndex = 0
offset = 0
for x in range(len(file[0])):
    allSpaces = True
    for y in range(len(file)):
        eIndex = x - offset
        element = file[y][x]
        if(element != " "):
            allSpaces = False
        if(len(values[blockIndex][1]) <= eIndex):
            values[blockIndex][1].append(element)
            continue
        values[blockIndex][1][eIndex] = values[blockIndex][1][eIndex] + element
    if(allSpaces == True or x == len(file[0])-1):
        if(x < len(file[0])-1):
            values[blockIndex][1].pop()
        if(values[blockIndex][0] == "+"):
            values[blockIndex].append(sum([int(x) for x in values[blockIndex][1]]))
        else:
            values[blockIndex].append(reduce(mul, [int(x) for x in values[blockIndex][1]]))
        blockIndex += 1
        offset = x+1

result = sum([x[2] for x in values])

print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)

# to low 13215665353940