from dataclasses import dataclass

@dataclass
class Vent:
    x1: int
    y1: int
    x2: int
    y2: int

    def getCoords(self):
        coords = []
        if (self.x1 == self.x2) and (self.y1 <= self.y2): # vertical, y2 higher
            for y in range(self.y1, self.y2 + 1):
                coords.append([self.x1, y])
        if (self.x1 == self.x2) and (self.y1 > self.y2): # vertical, y1 higher
            for y in range(self.y2, self.y1 + 1):
                coords.append([self.x1, y])
        if (self.y1 == self.y2) and (self.x1 <= self.x2): # horizontal, x2 higher
            for x in range(self.x1, self.x2 + 1):
                coords.append([x, self.y1])
        if (self.y1 == self.y2) and (self.x1 > self.x2): # horizontal, x1 higher
            for x in range(self.x2, self.x1 + 1):
                coords.append([x, self.y1])               

        return coords

vents = []

# Read File
with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        points = line[:-1].split(" -> ")
        point1 = [int(i) for i in points[0].split(",")]
        point2 = [int(i) for i in points[1].split(",")]
        vents.append(Vent(point1[0], point1[1], point2[0], point2[1]))

# Initialise coordinate map
coordMap = []
for y in range(1000):
    column = []
    for x in range(1000):
        column.append(0)
    coordMap.append(column)
   
# Get coordinates for each vent and put them on the map
for vent in vents:
    for coord in vent.getCoords():
        coordMap[coord[0]][coord[1]] = coordMap[coord[0]][coord[1]] + 1

# Count the intersections
intersectionCount = 0
for y in range(1000):
    for x in range(1000):
        if coordMap[x][y] > 1: 
            intersectionCount += 1

# Print Results
print("        Number of vents: %d" % len(vents))
print("Number of intersections: %d" % intersectionCount)
