heightMap = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        heightMap.append([int(i) for i in list(line[:-1])])

heightMapHeight = len(heightMap)
heightMapWidth = len(heightMap[0])
print("             Height map size: %d x %d" % (heightMapWidth, heightMapHeight))

lowPointCount = 0
riskLevelTotal = 0

for y in range(heightMapHeight):
    for x in range(heightMapWidth):
        pointToCheck = heightMap[y][x]
        lowerThanLeft = (x == 0) or pointToCheck < heightMap[y][x - 1]
        lowerThanRight = (x == heightMapWidth - 1) or pointToCheck < heightMap[y][x + 1]
        lowerThanUp = (y == 0) or pointToCheck < heightMap[y - 1][x]
        lowerThanDown = (y == heightMapHeight - 1) or pointToCheck < heightMap[y + 1][x]
        
        if lowerThanLeft and lowerThanRight and lowerThanUp and lowerThanDown:
            lowPointCount += 1
            riskLevelTotal += heightMap[y][x] + 1

print("         Count of low points: %d" % lowPointCount)
print("Sum of low point risk levels: %d" % riskLevelTotal)


        
