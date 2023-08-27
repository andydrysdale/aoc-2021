holes = []
folds = []

# Read the input file
with open("puzzledata.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        if line.startswith("fold"):
            folds.append(line.split()[2].split("="))
        else:
            linePartsAsString = line[:-1].split(",") 
            linePartsAsInt = [int(i) for i in linePartsAsString]
            holes.append(linePartsAsInt)

foldIterator = 0

for fold in folds:
    foldIterator += 1

    foldDirection = fold[0]
    foldLine = int(fold[1])
    folded = []

    for hole in holes:
        if foldDirection == "x":
            if hole[0] > foldLine:
                newX = (hole[0] - (foldLine * 2)) * -1
                folded.append([newX, hole[1]])
            else:
                folded.append(hole)
        elif foldDirection == "y":
            if hole[1] > foldLine:
                newY = (hole[1] - (foldLine * 2)) * -1
                folded.append([hole[0], newY])
            else:
                folded.append(hole)

    # remove duplicates
    foldedWithoutDuplicates = []
    for hole in folded:
        if hole not in foldedWithoutDuplicates: 
            foldedWithoutDuplicates.append(hole)

    # Print results of that fold
    print("Fold %d: %s%d" % (foldIterator, foldDirection, foldLine))
    print("Hole count after fold: %s" % len(foldedWithoutDuplicates))
    
    holes = foldedWithoutDuplicates.copy()

# Print the answer
maxX = 0
maxY = 0
for hole in holes:
    if hole[0] > maxX: maxX = hole[0]
    if hole[1] > maxY: maxY = hole[1]
print("maxX = %d, maxY = %d", (maxX, maxY))
for y in range(maxY + 1):
    for x in range(maxX + 1):
        checkForHole = [x, y]
        if checkForHole in holes:
            print("X", end="")
        else:
            print(" ", end="")
    print("")
