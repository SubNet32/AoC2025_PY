import time
from pathlib import Path 
from functools import cache
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

nodes = {}
nodeMap = {}

for i,line in enumerate(file):
    [node,connections] = line.split(": ")
    nodeMap[node] = 1 << i

nodeMap["out"] = 1 << i+1 

for i,line in enumerate(file):
    [node, connections] = line.split(": ")
    nodes[nodeMap[node]] = [nodeMap[x] for x in connections.split(" ")]



mustVisit = nodeMap["dac"] | nodeMap["fft"]

def solveFor(start, endS):
    end = nodeMap[endS]
    cache = {}
    def findPath(node, seen):
        if(node in cache):
            return cache[node]
      
        if(node == end):
            return 1
        if(node not in nodes):
            return 0
        
        result = 0
        for next in nodes[node]:
            if(next & seen > 0):
                continue
            result += findPath(next, seen | next)

        cache[node] = result
        return result
    
    return findPath(nodeMap[start], nodeMap[start])



a1 = solveFor("svr", "fft")
a2 = solveFor("fft", "dac")
a3 = solveFor("dac", "out")

b1 = solveFor("svr", "dac")
b2 = solveFor("dac", "fft")
b3 = solveFor("fft", "out")



print("--- %s seconds ---" % (time.time() - start_time))
print("result", a1*a2*a3 + b1*b2*b3)