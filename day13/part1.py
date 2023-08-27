holes = []
folds = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        if line.startswith("fold"):
            folds.append(line.split()[2].split("="))
        else:
            linePartsAsString = line[:-1].split(",") 
            linePartsAsInt = [int(i) for i in linePartsAsString]
            holes.append(linePartsAsInt)

folded = []
foldline = int(folds[0][1])

for hole in holes:
    if hole[0] > foldline:
        newX = (hole[0] - (foldline * 2)) * -1
        folded.append([newX, hole[1]])
    else:
        folded.append(hole)

# remove duplicates
foldedWithoutDuplicates = []
for hole in folded:
    if hole not in foldedWithoutDuplicates: 
        foldedWithoutDuplicates.append(hole)

print("Number of holes after fold and de-deplication:", len(foldedWithoutDuplicates))
