def checkChunk(expected, chunk):
    if len(chunk) == 0:
        return 0
    else:   
        firstOfChunk = chunk[0]
        if len(expected) > 0:
            lastOfExpected = expected[-1]
        else:
            lastOfExpected = ""

        if firstOfChunk == lastOfExpected: return checkChunk(expected[:-1], chunk[1:])
        elif firstOfChunk == "(": return checkChunk(expected + ")", chunk[1:])
        elif firstOfChunk == "[": return checkChunk(expected + "]", chunk[1:])
        elif firstOfChunk == "{": return checkChunk(expected + "}", chunk[1:])
        elif firstOfChunk == "<": return checkChunk(expected + ">", chunk[1:])
        elif firstOfChunk == ")": return 3
        elif firstOfChunk == "]": return 57
        elif firstOfChunk == "}": return 1197
        elif firstOfChunk == ">": return 25137



with open("puzzledata.txt", "r", encoding="utf-8") as file:
    scoreRunningTotal = 0

    for line in file.readlines():
        lineToCheck = line[:-1]
        scoreRunningTotal += checkChunk("", lineToCheck)
    
    print("Total syntax error score: %d" % scoreRunningTotal)
