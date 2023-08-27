with open("puzzledata.txt", "r", encoding="utf-8") as file:
    crabs = [int(i) for i in file.readline().split(",")]

    bestFuelUse = 9999999999999
    for pos in range(1000):
        totalFuelUse = 0
        for crab in crabs:
            distance = abs(crab - pos)
            totalFuelUse += (distance / 2) * (distance + 1)
        print("postion = %d, total fuel = %d" % (pos, totalFuelUse))
        if totalFuelUse < bestFuelUse:
            bestFuelUse = totalFuelUse

    print("Least possible fuel use: %d" % bestFuelUse)