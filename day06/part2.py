with open("puzzledata.txt", "r", encoding="utf-8") as file:
    fish = [int(i) for i in file.readline().split(",")]

    fishAtEachAge = [0,0,0,0,0,0,0,0,0]
    for f in fish:
        fishAtEachAge[f] = fishAtEachAge[f] + 1

    for day in range(256):
        numberAtZero = fishAtEachAge[0]
        for age in range(1,9):
            fishAtEachAge[age - 1] = fishAtEachAge[age]
        fishAtEachAge[8] = numberAtZero
        fishAtEachAge[6] = fishAtEachAge[6] + numberAtZero

    print("Number of fish: %d" % sum(fishAtEachAge))
        