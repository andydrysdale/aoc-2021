with open("puzzledata.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    lineLength = len(lines[0]) - 1
    runningTotals = [0] * lineLength

    for line in lines:
        for i in range(lineLength):
            if line[i] == "0":
                runningTotals[i] -= 1
            elif line[i] == "1":
                runningTotals[i] += 1

    gammaRate = 0
    epsilonRate = 0
    for j in range(lineLength):
        if(runningTotals[j] > 0):
            gammaRate += 2 ** (lineLength - j - 1)
        else:
            epsilonRate += 2 ** (lineLength - j - 1)
   
    print("  Gamma Rate: %d" % gammaRate)
    print("Epsilon Rate: %d" % epsilonRate)
    print("     Product: %d" % (gammaRate * epsilonRate))