import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

sum  = 0

def findLargest(line:str, remaining:int):
    largestValue = 0
    largestIndex = 0
    for i,vS in enumerate(line[:len(line)-remaining+1]):
        v = int(vS)
        if(v > largestValue):
            largestValue = v 
            largestIndex = i
    return (largestValue, largestIndex)


for line in file:
    remaining = 12
    result = ""
    index = 0
    while(remaining > 0):
        (value, newIndex) = findLargest(line[index:], remaining)
        result += str(value)
        index += newIndex+1
        remaining -= 1
    sum += int(result)


print("--- %s seconds ---" % (time.time() - start_time))
print("result", sum)

# too high 171735739026999