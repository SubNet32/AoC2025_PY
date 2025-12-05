import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

ranges = []

isId = False
result = 0
for line in file:
    if(line == ""):
        isId = True
        continue
    if(isId == False):
        [s,e] = [int(x) for x in line.split("-")]
        ranges.append(range(s,e+1))
        continue

    id = int(line)
    if(any(id in r for r in ranges)):
        result+= 1
        continue



print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)