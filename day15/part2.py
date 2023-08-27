cavern = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        cavern.append([int(i) for i in list(line[:-1])])

cavernWidth = len(cavern[0])
cavernHeight = len(cavern)
print("cavern size = %d x %d" % (cavernWidth, cavernHeight))

bigCavern = []
for y in range(cavernHeight * 5):
    row = []
    for x in range(cavernWidth * 5):
        value = cavern[y % cavernHeight][x % cavernWidth] + (y // cavernHeight) + (x // cavernWidth)
        if value > 9: value -= 9
        row.append(value)
    bigCavern.append(row)
        
bigCavernHeight = len(bigCavern)
bigCavernWidth = len(bigCavern[0])
print("Big cavern size = %d x %d" % (bigCavernWidth, bigCavernHeight))

print("Calculating route...")


for backCounter in range((bigCavernHeight + bigCavernWidth - 3), -1, -1):
    print(backCounter)
    for y in range(bigCavernHeight):
        for x in range(bigCavernWidth):
            if y + x == backCounter:
                right = 999999999999
                down = 999999999999
                if x < bigCavernWidth - 1: right = bigCavern[y][x+1]
                if y < bigCavernHeight - 1: down = bigCavern[y+1][x]
                if right < down:
                    bigCavern[y][x] = bigCavern[y][x] + bigCavern[y][x+1]
                else:
                    bigCavern[y][x] = bigCavern[y][x] + bigCavern[y+1][x]

print(bigCavern[0][1])
print(bigCavern[1][0])
print(bigCavern[0][0])
print(bigCavern)
        

