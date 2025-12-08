import time
import math
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

def getDistance(p1:tuple[int,int,int], p2: tuple[int,int,int]):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return dx*dx + dy*dy + dz*dz

class DSU:
    def __init__(self, points:list[tuple]):
        self.parent = {p: p for p in points}
        self.rank = {p: 0 for p in points}
        self.count = len(points)

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  
        return self.parent[p]
    
    def merge(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        self.count -= 1
        return True


points = [(int(x),int(y),int(z)) for [x,y,z] in (line.split(",") for line in file)]

distances = []
N = len(points)
for i in range(N):
    for j in range(i+1, N):
        p1 = points[i]
        p2 = points[j]
        distances.append((getDistance(p1,p2), p1, p2))

distances.sort(key=lambda x: x[0])

dsu = DSU(points)

touched = set()
allConnected = False
result = 0
for _, p1, p2 in distances:
    touched.add(p1)
    touched.add(p2)

    dsu.merge(p1,p2)

    if(allConnected == False and len(touched) == N):
        allConnected = True
    if(allConnected and dsu.count == 1):
        result = p1[0] * p2[0]
        break


print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)