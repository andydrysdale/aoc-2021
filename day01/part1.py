with open("puzzledata.txt", "r", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    
    largerThanPreviousCount = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            largerThanPreviousCount += 1 

    print(largerThanPreviousCount)