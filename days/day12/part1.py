import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

shapes = []
regions = []

currentShape = []
for line in file:
    if(line == ""):
        if(len(currentShape)>0):
            spaceReq = sum([1 for x in [x for sub in currentShape for x in sub] if x == "#" ])
            shapes.append((currentShape, spaceReq))
            currentShape = []
        continue
    if("x" in line):
        [size, count] = line.split(": ")
        [xs,ys] = [int(x) for x in size.split("x")]
        values = [int(x) for x in count.split()]
        regions.append(((xs,ys), values))
        continue
    if(":" in line):
        continue
    currentShape.append(line)


def solveRegion(region: tuple[tuple[int], list[int]]):
    ((xs,ys), values) = region
    totalSpace = xs * ys
    reqSpace = 0
    for i,v in enumerate(values):
        reqSpace += v * shapes[i][1]

    return totalSpace >= reqSpace


result = len([1 for r in regions if solveRegion(r)])


print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)