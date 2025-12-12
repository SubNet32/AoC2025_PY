import time
import z3
from pathlib import Path 

start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
def parseLine(line: str):
    [_, rest] = line.replace("[", "").split("] ")
    [buttonsStr, joltage] = rest.replace("}", "").split(" {")

    buttons = buttonsStr.strip().split(" ")

    buttonValues = []
    for button in buttons:
        buttonValues.append([int(x) for x in button.replace("(", "").replace(")", "").split(",")])

    joltageValues = [int(x) for x in joltage.split(",")]

    buttonAdder = []
    for b in buttonValues:
        a = [1 if i in b else 0 for i in range(len(joltageValues))]
        buttonAdder.append(tuple(a))

    return (tuple(joltageValues), buttonAdder)


def solve(line):
    requirement, buttons = parseLine(line)
    lenReq = len(requirement)
    lenButtons = len(buttons)

    x = [z3.Int(f"x_{i}") for i in range(lenButtons)]
    solver = z3.Optimize()

    # add constraint >= 0
    for xi in x:
        solver.add(xi >= 0)

    # add button presses = requirement
    for d in range(lenReq):
        solver.add(z3.Sum([buttons[i][d] * x[i] for i in range(lenButtons)]) == requirement[d])

    # find minimal solution
    solver.minimize(z3.Sum(x))

    solver.check()
    model = solver.model()
    total = sum(model[xi].as_long() for xi in x)

    return total


presses = 0
for line in file:
    presses += solve(line)

print("--- %s seconds ---" % (time.time() - start_time))
print("result", presses)
