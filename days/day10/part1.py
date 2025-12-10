import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

def parseLine(line:str):
    [indicator, rest] = line.replace("[","").split("] ")
    [buttonsStr, _joltage] = rest.replace("}", "").split(" {")
    buttons = buttonsStr.strip().split(" ")

    indicatorValue = int(indicator[::-1].replace("#","1").replace(".","0"), 2)
    buttonValues = []
    for button in buttons:
        terms = button[1:-1].split(",")
        value = 0
        for t in terms:
            value += 2 ** int(t)
        buttonValues.append(value)

    return (indicatorValue, buttonValues)


presses = 0
for line in file:
    (requirement, buttons) = parseLine(line)
    # to test = (button to test, result, previous Button used)
    toTest = [(x, 0, None) for x in buttons]
    depth = 0
    foundResult = False
    while(not foundResult):
        nextTest = []
        depth += 1
        for (button, value, prev) in toTest:
            result = value ^ button
            if(result == requirement):
                presses += depth
                foundResult = True
                break
            for tb in buttons:
                if(tb == prev):
                    continue
                nextTest.append((tb, result, button))
        toTest = nextTest




print("--- %s seconds ---" % (time.time() - start_time))
print("result", presses)