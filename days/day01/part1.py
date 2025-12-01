import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

pos = 50
zeroCount = 0

for line in file: 
    dir = line[0]
    value = int(line[1:])

    if dir == "L":
        pos -= value
        while(pos < 0):
            pos += 100
    else :
        pos += value
        while(pos > 99):
            pos -= 100
    if pos == 0:
        zeroCount += 1
        
print("--- %s seconds ---" % (time.time() - start_time))
print("result", zeroCount)