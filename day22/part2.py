import re
import time
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
        for z in range(startZ, endZ + 1):
            for y in range(startY, endY + 1):
                for x in range(startX, endX + 1):
                    coords.append(str(z) + " " + str(y) + " " + str(z))
        return coords

    def getIsTurnOn(self):
        return self.turnOn

cubes = []

# Read File
with open("testdata3.txt", "r", encoding="utf-8") as file:
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

coordsOn = set()

for cube in cubes:
    startTime = time.perf_counter()
    print("=====================================================")
    print("                 cube =", cube)
    print("   initial squares on =", len(coordsOn))
    for coord in cube.getCoords():
        if cube.getIsTurnOn():
            coordsOn.add(coord)
        else:
            coordsOn.discard(coord)
    print("elapsed time for cube =", time.perf_counter() - startTime)

onCount = len(coordsOn)

print("total on =", onCount)
