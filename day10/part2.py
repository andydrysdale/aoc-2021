def checkChunk(expected, chunk):
    if len(chunk) == 0:
        score = 0
        for i in expected:
            score *= 5
            if i == ")": score += 1
            elif i == "]": score += 2
            elif i == "}": score += 3
            elif i == ">": score += 4
        return score
    else:   
        firstOfChunk = chunk[0]
        if len(expected) > 0:
            firstOfExpected = expected[0]
        else:
            firstOfExpected = ""

        if firstOfChunk == firstOfExpected: return checkChunk(expected[1:], chunk[1:])
        elif firstOfChunk == "(": return checkChunk(")" + expected, chunk[1:])
        elif firstOfChunk == "[": return checkChunk("]" + expected, chunk[1:])
        elif firstOfChunk == "{": return checkChunk("}" + expected, chunk[1:])
        elif firstOfChunk == "<": return checkChunk(">" + expected, chunk[1:])
        elif firstOfChunk == ")": return None
        elif firstOfChunk == "]": return None
        elif firstOfChunk == "}": return None
        elif firstOfChunk == ">": return None


with open("puzzledata.txt", "r", encoding="utf-8") as file:
    scores = []

    for line in file.readlines():
        lineToCheck = line[:-1]
        score = checkChunk("", lineToCheck)
        if score != None: scores.append(score)
    
    scores.sort()
    print("Middle score: %d" % scores[len(scores) // 2])