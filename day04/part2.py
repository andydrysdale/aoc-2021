from dataclasses import dataclass
from typing import List

@dataclass
class BingoCard:
    data: List[List[int]]
    hasWon: bool

    def checkForWin(self, listOfNumbers):
        if not self.hasWon:
            win = False
            for i in range(5):
                if all(elem in listOfNumbers for elem in self.data[i]):
                    win = True
                if all(elem in listOfNumbers for elem in [self.data[0][i],self.data[1][i],self.data[2][i],self.data[3][i],self.data[4][i]]):
                    win = True
            if win:
                self.hasWon = True
                flattenedListOfNumbers = [item for sublist in self.data for item in sublist]
                unmarkedData = [x for x in flattenedListOfNumbers if x not in listOfNumbers]
                sumOfUnmarkedData = sum(unmarkedData)
                lastNumberDrawn = listOfNumbers[-1]
                print("Sum of unmarked numbers: %d" % sumOfUnmarkedData)
                print("      Last number drawn: %d" % lastNumberDrawn)
                print("                Product: %d" % (sumOfUnmarkedData * lastNumberDrawn))


numbersToDraw = []
bingoCards = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    numbersToDraw = [int(i) for i in lines[0][:-1].split(",")]

    for lineNo in range(1, len(lines), 6):
        tempBingoCard = BingoCard([[int(i) for i in lines[lineNo + 1][:-1].split()],
                                   [int(i) for i in lines[lineNo + 2][:-1].split()],
                                   [int(i) for i in lines[lineNo + 3][:-1].split()],
                                   [int(i) for i in lines[lineNo + 4][:-1].split()],
                                   [int(i) for i in lines[lineNo + 5][:-1].split()]],
                                   False)
        bingoCards.append(tempBingoCard)

numbersToCheckAgainst = []
for i in range(len(numbersToDraw)):
    numbersToCheckAgainst.append(numbersToDraw[i])
    for card in bingoCards:
        card.checkForWin(numbersToCheckAgainst)
          
