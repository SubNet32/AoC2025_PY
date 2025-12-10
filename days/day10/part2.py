import time
from pathlib import Path 
from collections import deque
from multiprocessing import Pool

start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}


def parseLine(line:str):
    [_, rest] = line.replace("[","").split("] ")
    [buttonsStr, joltage] = rest.replace("}", "").split(" {")
    buttons = buttonsStr.strip().split(" ")


    buttonValues = []
    for button in buttons:
        buttonValues.append([int(x) for x in button.replace("(","").replace(")","").split(",")])

    joltageValues = [int(x) for x in joltage.split(",")]
    buttonAdder = []
    for b in buttonValues:
        a = [1 if i in b else 0 for i in range(len(joltageValues))]
        buttonAdder.append(tuple(a))
 
    return (tuple(joltageValues), buttonAdder)


def solve(line):
    (requirement, buttons) = parseLine(line)
    start = tuple([0 for _ in range(len(requirement))])
    bN = len(buttons)
    
    seen = set([start])
    start_time2 = time.time()
    queue = deque([(start, 1, 0)])

    while(queue):
        counter, depth, buttonIndex = queue.popleft()
        for bi in range(buttonIndex, bN):
            button = buttons[bi]
            newCounter = tuple(c + bi for c, bi in zip(counter, button))
            if(newCounter in seen):
                continue
            if any(nc > r for nc, r in zip(newCounter, requirement)):
                continue
            if(newCounter == requirement):
                print("--- %s seconds ---" % (time.time() - start_time2))
                print("Found result after presses", depth)
                return depth
            seen.add(newCounter)
            queue.append((newCounter, depth+1, buttonIndex if bi == buttonIndex else buttonIndex+1 ))


if __name__ == "__main__":
    with Pool(processes=18) as pool:  # adjust to your CPU cores
        results = pool.map(solve, file)

    presses = sum(results)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("result", presses)
