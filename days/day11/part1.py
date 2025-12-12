import time
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

nodes = {}

for line in file:
    [node, connections] = line.split(": ")
    nodes[node] = [x for x in connections.split(" ")]


start = "you"
end = "out"

def findPath(node):
    if(node == end):
        return 1
    result = 0
    for next in nodes[node]:
        result += findPath(next)
    return result


result = findPath(start)


print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)