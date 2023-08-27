import re
from dataclasses import dataclass

@dataclass
class Cube:
    turnOn: bool
    xMin: int
    xMax: int
    yMin: int
    yMax: int
    zMin: int
    zMax: int

    def getCoords(self):
        coords = []

        startZ = self.zMin
        endZ = self.zMax
        startY = self.yMin
        endY = self.yMax
        startX = self.xMin
        endX = self.xMax
        if startZ <= 50 and endZ >= -50:
            if startZ < -50: startZ = -50
            if endZ > 50: endZ = -50
            if startY <= 50 and endY >= -50:
                if startY < -50: startY = -50
                if endY > 50: endY = -50
                if startX <= 50 and endX >= -50:
                    if startX < -50: startX = -50
                    if endX > 50: endX = -50
                    for z in range(startZ, endZ + 1):
                        for y in range(startY, endY + 1):
                            for x in range(startX, endX + 1):
                                coords.append([z+50, y+50, x+50])
        return coords

    def getIsTurnOn(self):
        return self.turnOn

cubes = []

# Read File
with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        lineParts = re.split(" |,|=|x|y|z|\.|\n", line)
        if lineParts[0] == "on": 
            turnOn = True
        else:
            turnOn = False
        cubes.append(Cube(turnOn, 
                          int(lineParts[3]),
                          int(lineParts[5]),
                          int(lineParts[8]),
                          int(lineParts[10]),
                          int(lineParts[13]), 
                          int(lineParts[15])))

reactor = []
for z in range(101):
    plane = []
    for y in range(101):
        row = []
        for x in range(101):
            row.append(False)
        plane.append(row)
    reactor.append(plane)

for cube in cubes:
    print(cube)
    for coord in cube.getCoords():
        reactor[coord[0]][coord[1]][coord[2]] = cube.getIsTurnOn()

onCount = 0
for z in range(101):
    for y in range(101):
        for x in range(101):
            if reactor[z][y][x]: onCount += 1

print("total on =", onCount)
