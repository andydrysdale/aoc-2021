cavern = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        cavern.append([int(i) for i in list(line[:-1])])

print(cavern)
cavernWidth = len(cavern[0])
cavernHeight = len(cavern)
print("cavern size = %d x %d" % (cavernWidth, cavernHeight))


for backCounter in range((cavernHeight  + cavernWidth - 3), -1, -1):
    print(backCounter)
    for y in range(cavernHeight):
        for x in range(cavernWidth):
            if y + x == backCounter:
                print("x=%d, y = %d" % (x,y))
                right = 999999999999
                down = 999999999999
                if x < cavernWidth - 1: right = cavern[y][x+1]
                if y < cavernHeight - 1: down = cavern[y+1][x]
                if right < down:
                    cavern[y][x] = cavern[y][x] + cavern[y][x+1]
                else:
                    cavern[y][x] = cavern[y][x] + cavern[y+1][x]
                    
print(cavern)
        

