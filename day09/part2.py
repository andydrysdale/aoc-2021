heightMap = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        heightMap.append([int(i) for i in list(line[:-1])])

heightMapHeight = len(heightMap)
heightMapWidth = len(heightMap[0])

basinSizes = []

for y in range(heightMapHeight):
    for x in range(heightMapWidth):
        pointToCheck = heightMap[y][x]
        lowerThanLeft = (x == 0) or pointToCheck < heightMap[y][x - 1]
        lowerThanRight = (x == heightMapWidth - 1) or pointToCheck < heightMap[y][x + 1]
        lowerThanDown = (y == 0) or pointToCheck < heightMap[y - 1][x]
        lowerThanUp = (y == heightMapHeight - 1) or pointToCheck < heightMap[y + 1][x]
        
        if lowerThanLeft and lowerThanRight and lowerThanDown and lowerThanUp: # if low point
            basinSize = 0

            # this function is used to recursivly check if the surrounding points are in the same basin
            def checkSurroundingPoints(x, y, basinSize):
                if heightMap[y][x] != 9:
                    basinSize += 1
                    heightMap[y][x] = 9 # stop this point being read again
                    if x != 0: 
                        basinSize = checkSurroundingPoints(x - 1, y, basinSize) # left
                    if x != (heightMapWidth - 1): 
                        basinSize = checkSurroundingPoints(x + 1, y, basinSize) # right
                    if y != 0: 
                        basinSize = checkSurroundingPoints(x, y - 1, basinSize) # down
                    if y != (heightMapHeight - 1):
                        basinSize = checkSurroundingPoints(x, y + 1, basinSize) # up
                return basinSize

            # Use the low point coordinates as the starting point for the recursive basin check
            basinSize = checkSurroundingPoints(x, y, basinSize)

            basinSizes.append(basinSize)

basinSizes.sort(reverse = True)
productOfLargestBasins = basinSizes[0] * basinSizes[1] * basinSizes[2]

print("Product of 3 largest basin sizes: %d" % productOfLargestBasins)
