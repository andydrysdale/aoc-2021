with open("puzzledata.txt", "r", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    
    largerThanPreviousCount = 0
    for i in range(len(data) - 3):
        firstThreeTotal = data[i] + data[i+1] + data[i+2]
        secondThreeTotal = data[i+1] + data[i+2] + data[i+3]
        if secondThreeTotal > firstThreeTotal:
            largerThanPreviousCount += 1 

    print(largerThanPreviousCount)