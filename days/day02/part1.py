import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

ids = file[0].split(",")

def isInvalid(number:str):
    numberLen = len(number)
    if(numberLen % 2 != 0):
        return False
    half = int(numberLen/2)
    first = number[0:half]
    last = number[half:]
    return first == last

sum = 0
for id in ids:
    [a,b] = [int(x) for x in id.split("-") ]
    for value in range(a,b):
        if(isInvalid(str(value))):
            sum += value
            print("Found invalid id", value)
        value += 1
    


print("--- %s seconds ---" % (time.time() - start_time))
print("result", sum)