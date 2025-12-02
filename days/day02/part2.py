import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

ids = file[0].split(",")

def consistOnlyOf(value: str, expression:str):
    if(len(value) % len(expression) != 0):
        return False
    factor = int(len(value) / len(expression))
    return expression * factor == value
    
def isInvalid(number:str):
    if(len(number) == 1):
        return False
    expression = ""
    while(len(expression) < len(number)):
        expression += number[0]
        number = number[1:]
        if(consistOnlyOf(number, expression)):
            return True
    return False
        
sum = 0
for id in ids:
    [a,b] = [int(x) for x in id.split("-") ]
    for value in range(a,b):
        if(isInvalid(str(value))):
            sum += value
        value += 1
    

print("--- %s seconds ---" % (time.time() - start_time))
print("result", sum)

# too high 31578210067