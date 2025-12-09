import time
import math
from pathlib import Path 
start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

points = [(int(x),int(y)) for [x,y] in (line.split(",") for line in file)]

def getArea(p1:tuple, p2:tuple):
  return (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1) 

largestArea = 0
N = len(points)
for i in range(N-1):
  for j in range(i+1, N):
    largestArea = max(largestArea, getArea(points[i], points[j]))


print("--- %s seconds ---" % (time.time() - start_time))
print("result", largestArea)