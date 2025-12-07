import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

beams = set()

beams.add(file.pop(0).find("S"))

splitCounter = 0
for line in file:
    splitters = [i for i,x in enumerate(line) if x == "^" ]
    oldBeams = beams.copy()
    newBeams = set()
    for s in splitters:
        if(s not in oldBeams):
            continue
        splitCounter+=1
        oldBeams.remove(s)
        newBeams.add(s-1)
        newBeams.add(s+1)
    beams = newBeams.union(oldBeams)




print("--- %s seconds ---" % (time.time() - start_time))
print("result", splitCounter)