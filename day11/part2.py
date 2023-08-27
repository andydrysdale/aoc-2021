octopuses = []

# Increases the energy levels of all octopuses by 1
def increaseEnergyLevels():
    for y in range(10):
        for x in range(10):
            octopuses[y][x] += 1

# If any octopus has an energy level of >9 it has 'flashed'. This means the 
# energy state of its neighbours is increases by 1. The flashed octopus' 
# energy level is set to -9999 so that it doesn't flash again in the same step.
def checkForFlashes():
    flashCount = 0
    for y in range(10):
        for x in range(10):
            if octopuses[y][x] > 9:
                flashCount += 1
                octopuses[y][x] = -9999
                if x > 0: octopuses[y][x-1] += 1 #left
                if x < 9: octopuses[y][x+1] += 1 #right
                if y > 0: octopuses[y-1][x] += 1 #down
                if y < 9: octopuses[y+1][x] += 1 #up
                if x > 0 and y > 0: octopuses[y - 1][x - 1] += 1 #down, left                
                if x > 0 and y < 9: octopuses[y + 1][x - 1] += 1 #up, left                
                if x < 9 and y > 0: octopuses[y - 1][x + 1] += 1 #down, right                
                if x < 9 and y < 9: octopuses[y + 1][x + 1] += 1 #up, right
    return flashCount 

# Reset all 'flashed' octupuses (energy level < 0) to a zero energy level.
def resetFlashedOctopuses():
    for y in range(10):
        for x in range(10):
            if octopuses[y][x] < 0: octopuses [y][x] = 0

# Returns True if all octopus energy levels are 0.
def checkIfSynched():
    synched = True
    for y in range(10):
        for x in range(10):
            if octopuses[y][x] != 0: synched = False
    return synched


# Read the input file
with open("puzzledata.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        octopuses.append([int(i) for i in list(line[:-1])])

for step in range(1000):
    if checkIfSynched():
        print("Octopus energy levels synched on step %d" % step)
        exit(0)

    increaseEnergyLevels()

    flashesStopped = False
    while not flashesStopped:
        flashCount = checkForFlashes()
        if flashCount == 0: flashesStopped = True

    resetFlashedOctopuses()



