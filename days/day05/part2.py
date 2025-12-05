import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

ranges = []

def overlaps(a:range, b:range):
    return a.start <= b.stop and b.start <= a.stop

file.sort()

for line in file:
    if("-" not in line):
        continue
 
    [s,e] = [int(x) for x in line.split("-")]
    newRange = range(s,e)
    wasMerged = False
    for r in ranges:
        if(overlaps(r, newRange)):
            ranges.append(range(min(r.start, newRange.start), max(r.stop, newRange.stop)))
            ranges.remove(r)
            wasMerged=True
            break
    if(wasMerged == False):
        ranges.append(newRange)

result = 0
for range in ranges:
    result += (range.stop) - range.start + 1

print(ranges)

print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)
