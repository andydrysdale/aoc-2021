with open("puzzledata.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    lineLength = len(lines[0]) - 1

    # Oxygen Generator Rating
    linesToKeep = lines
    for i in range(lineLength):
        mostCommon = 0
        for line in linesToKeep:
            if line[i] == "0":
                mostCommon -= 1
            elif line[i] == "1":
                mostCommon += 1
        tempLines = []
        for line in linesToKeep:
            if mostCommon >= 0 and line[i] == "1":
                tempLines.append(line)
            elif mostCommon < 0 and line[i] == "0":
                tempLines.append(line)
        linesToKeep = tempLines
        if len(linesToKeep) == 1: break
    oxygen = int(linesToKeep[0], 2)
    print("Oxygen Generator Rating: %d" % oxygen)

    # CO2 Scrubber Rating Rating
    linesToKeep = lines
    for i in range(lineLength):
        mostCommon = 0
        for line in linesToKeep:
            if line[i] == "0":
                mostCommon -= 1
            elif line[i] == "1":
                mostCommon += 1
        tempLines = []
        for line in linesToKeep:
            if mostCommon < 0 and line[i] == "1":
                tempLines.append(line)
            elif mostCommon >= 0 and line[i] == "0":
                tempLines.append(line)
        linesToKeep = tempLines
        if len(linesToKeep) == 1: break
    scrubber = int(linesToKeep[0], 2)
    print("    CO2 Scrubber Rating: %d" % scrubber) 

    # Life Support Rating
    print("    Life Support Rating: %d" % (oxygen * scrubber))