import time
from pathlib import Path

start_time = time.time()
cwd = Path(__file__).parent
path = cwd.joinpath("input.txt")
file = open(path, "r").read().splitlines()

points = [(int(x), int(y)) for [x, y] in (line.strip().split(",") for line in file if line.strip())]
N = len(points)

edges = []
for i in range(N):
    a = points[i]
    b = points[(i + 1) % N]
    edges.append((a, b))

def getArea(p1:tuple, p2:tuple):
  return (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1) 

def createRect(p1, p2):
    x1 = min(p1[0], p2[0])
    x2 = max(p1[0], p2[0])
    y1 = min(p1[1], p2[1])
    y2 = max(p1[1], p2[1])
    return (x1, y1, x2, y2)

def pointOnBorder(x, y):
    for (x1, y1), (x2, y2) in edges:
        if x1 == x2 == x and min(y1, y2) <= y <= max(y1, y2):
            return True
        if y1 == y2 == y and min(x1, x2) <= x <= max(x1, x2):
            return True
    return False

def pointIsInsidePolygon(x, y):
    # raycasting test
    inside = False
    for  ((x1, y1), (x2, y2)) in edges:
        if ((y1 > y) != (y2 > y)):
            r = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if x < r:
                inside = not inside
    return inside

def reactIntersectsEdge(rect):
    (rx1, ry1, rx2, ry2) = rect
    for (x1, y1), (x2, y2) in edges:

      # vertical edge
      if x1 == x2:
          x = x1
          if rx1 < x < rx2:
              y_low = min(y1, y2)
              y_high = max(y1, y2)
              if y_high > ry1 and y_low < ry2:
                  return True
          continue

      # horizontal edge
      y = y1
      if ry1 < y < ry2:
          x_low = min(x1, x2)
          x_high = max(x1, x2)
          if x_high > rx1 and x_low < rx2:
              return True
      continue
    return False


areas = []
for i in range(N-1):
  for j in range(i+1, N):
    areas.append((getArea(points[i], points[j]), points[i], points[j]))

areas.sort()

while(True):
        (area, p1,p2) = areas.pop()
       
        rect = createRect(p1, p2)
        (rx1, ry1, rx2, ry2) = rect
        corners = [(rx1, ry1), (rx1, ry2), (rx2, ry1), (rx2, ry2)]

        # check if all corners are inside the polygon
        ok = True
        for (x,y) in corners:
            if(not (pointOnBorder(x, y) or pointIsInsidePolygon(x, y))):
                ok = False
                break
            
        if(not ok):
            continue

        # check if any edges intersect
        if(not reactIntersectsEdge(rect)):
          result = area
          break
         
             

print("--- %s seconds ---" % (time.time() - start_time))
print("result", result)
