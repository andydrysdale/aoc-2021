player1Number = 6
player2Number = 1
player1Total = 0
player2Total = 0
diceSize = 100
diceValue = 0
targetScore = 1000
player1 = True
winnerFound = False

while not winnerFound:
    diceNumberToAdd = ((diceValue % 100) * 3) + 6
    print(diceNumberToAdd)
    diceValue += 3

    if player1:
        player1Number += diceNumberToAdd
        while player1Number > 10: player1Number -= 10
        player1Total += player1Number
        print("p1", player1Total)
        if player1Total >= targetScore:
            print("player 1 wins!")
            print("==============")
            print("player 2 score =", player2Total)
            print("last dice roll =", diceValue)
            print("product = ", player2Total * diceValue)
            winnerFound = True
        player1 = False
    else:
        player2Number += diceNumberToAdd
        while player2Number > 10: player2Number -= 10
        player2Total += player2Number
        print("p2", player2Total)
        if player2Total >= targetScore:
            print("player 2 wins!")
            print("==============")
            print("player 1 score =", player1Total)
            print("last dice roll =", diceValue)
            print("product = ", player1Total * diceValue)
            winnerFound = True
        player1 = True
