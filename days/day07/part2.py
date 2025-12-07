import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()



cache = {}

def calcResult(beam:int, index:int):
    if(index >= len(file)):
        return 1
    if((beam, index) in cache):
        return cache[(beam, index)]
    result = 0
    if(file[index][beam] == "^"):
        result += calcResult(beam-1, index+1) 
        result += calcResult(beam+1, index+1) 
    else:
       result += calcResult(beam, index+1)     
          
    cache[(beam, index)] = result
    return result

startBeam = file.pop(0).find("S")
startLine = next((i for i, x in enumerate(file) if "^" in x))
totalWorlds = calcResult(startBeam,startLine)


print("--- %s seconds ---" % (time.time() - start_time))
print("result", totalWorlds)