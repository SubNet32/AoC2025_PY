import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

dirs = [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1,-1), (1, 0), (1, 1)]

map = {}

def getAdjacentRolls(x:int,y:int):
    count = 0
    for dir in dirs:
        cX = x + dir[0]
        cY = y + dir[1]
        if((cX, cY) in map):
            count += 1
    return count


result = 0
for y, line in enumerate(file):
    for x, v in enumerate(line):
        if(v == "@"):
            map[(x,y)] = 1

for p in map:
    if(getAdjacentRolls(p[0],p[1]) < 4):
        result += 1







print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)