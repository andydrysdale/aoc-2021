with open("puzzledata.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        lineparts = line.split()
        for i in range(11, 15):
            if len(lineparts[i]) == 2 or len(lineparts[i]) == 3 or len(lineparts[i]) == 4 or len(lineparts[i]) == 7:
                count += 1
    print("Total count of unique length numbers: %d" % count)