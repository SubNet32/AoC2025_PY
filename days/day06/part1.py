import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

file.reverse()

result = [[x, 1 if x == "*" else 0] for x in file.pop(0).split() if x != ""]

for line in file:
    elements = [x for x in line.split() if x != ""]
    for i,e in enumerate(elements):
        if(result[i][0] == "*"):
            result[i][1] = result[i][1] * int(e)
        else:
            result[i][1] = result[i][1] + int(e)


total = sum([x[1] for x in result])

print("--- %s seconds ---" % (time.time() - start_time))
print("result", total)