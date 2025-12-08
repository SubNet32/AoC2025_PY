import time
import math
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

def getDistance(p1:tuple[int,int,int], p2: tuple[int,int,int]):
    return math.sqrt(math.pow(p1[0]-p2[0],2) + math.pow(p1[1]-p2[1],2) + math.pow(p1[2]-p2[2],2))


points = {}


for line in file:
    [x,y,z] = [int(c) for c in line.split(",")]
    points[(x,y,z)] = 0

checkedPoints = set()
distances = []
for p1 in points:
    for p2 in points:
        if(p1 == p2 or (p1,p2) in checkedPoints or (p2,p1) in checkedPoints):
            continue
        checkedPoints.add((p1,p2))
        distances.append([getDistance(p1,p2),p1,p2])

distances.sort(key=lambda x: x[0])

circuits : dict[int,list] = {}
circuitId = 0
for _ in range(10 if len(file) < 100 else 1000):
    [_,p1,p2] = distances.pop(0)
    c1 = points[p1]
    c2 = points[p2]

    if(c1 == 0 and c2 == 0):
        circuitId += 1
        points[p1] = circuitId
        points[p2] = circuitId
        circuits[circuitId] = [p1,p2]
        continue

    if(c1 == 0):
        points[p1] = c2
        circuits[c2].append(p1)
        continue
    
    if(c2 == 0):
        points[p2] = c1
        circuits[c1].append(p2)
        continue

    if(c1 == c2):
        continue
    # move all points to the same circuit
    circuits[c1].extend(circuits[c2])
    for p in circuits[c2]:
        points[p] = c1
    del circuits[c2]

lengths =  [len(x) for x in circuits.values()]
lengths.sort()

result = lengths[-1] * lengths[-2] * lengths[-3] 

print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)