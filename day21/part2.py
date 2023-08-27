currentNumber = [4,8]
runningTotal = [0,0]
turnCount = [0,0]
reachedTarget = [False, False]
targetScore = 21

turns = 0

while not reachedTarget[0] and not reachedTarget[1]:
    for p in range(2):
        turns += 1
        possibleRolls = [3, 4, 5, 6, 7, 8, 9]
        possibleScores = []
        for roll in possibleRolls:
            score = currentNumber[p] + roll + 1
            if score > 10: score -= 10
            possibleScores.append(score)
        print("possible scores:", possibleScores)
        runningTotal[p] += max(possibleScores)
        turnCount[p] += 1
        print("player %d running total after %d turns = %d" % (p + 1, turnCount[p], runningTotal[p]))
        print(27 ** turns)
        if runningTotal[p] >= targetScore: reachedTarget[p] = True

print("Total turns = ", turns)
            
        
        


        

