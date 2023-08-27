with open("puzzledata.txt", "r", encoding="utf-8") as file:
    fish = [int(i) for i in file.readline().split(",")]

    for day in range(80):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] = fish[i] - 1

    print("Number of fish: %d" % len(fish))