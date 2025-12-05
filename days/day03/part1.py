import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

sum  = 0

for line in file:
    largestValue = 0
    largestIndex = 0
    for i,vS in enumerate(line[:-1]):
        v = int(vS)
        if(v > largestValue):
            largestValue = v 
            largestIndex = i

    secondLargestValue = 0
    for v in [int(x) for x in line[largestIndex+1:]]:

        if(v > secondLargestValue):
            secondLargestValue = v 
    sum += int(largestValue*10+secondLargestValue)


print("--- %s seconds ---" % (time.time() - start_time))
print("result", sum)