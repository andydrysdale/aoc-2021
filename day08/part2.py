with open("puzzledata.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        lineparts = line.split()
        lettersInDigit = [[],[],[],[],[],[],[],[],[],[]]

        # Unique length numbers
        for i in range(10):
            if len(lineparts[i]) == 2: lettersInDigit[1] = list(lineparts[i])
            if len(lineparts[i]) == 3: lettersInDigit[7] = list(lineparts[i])
            if len(lineparts[i]) == 4: lettersInDigit[4] = list(lineparts[i])
            if len(lineparts[i]) == 7: lettersInDigit[8] = list(lineparts[i]) 
        # If it has 6 segments that include the all 4 segments from number 4, it must be 9
        for i in range(10):
            if len(lineparts[i]) == 6 and all(elem in list(lineparts[i]) for elem in lettersInDigit[4]):
                lettersInDigit[9] = list(lineparts[i])
        # If it has 6 segments, the both segments from number 1 and is not 9, it must be 0
        for i in range(10):
            if len(lineparts[i]) == 6 and all(elem in list(lineparts[i]) for elem in lettersInDigit[1]) and not all(elem in list(lineparts[i]) for elem in lettersInDigit[9]):
                lettersInDigit[0] = list(lineparts[i])
        # If it has 6 segments and isn't 9 or 0, it must be 6
        for i in range(10):
            if len(lineparts[i]) == 6 and not all(elem in list(lineparts[i]) for elem in lettersInDigit[9]) and not all(elem in list(lineparts[i]) for elem in lettersInDigit[0]):
                lettersInDigit[6] = list(lineparts[i])
        # If it has 5 segments that include all the segments from number 7, it must be 3
        for i in range(10):
            if len(lineparts[i]) == 5 and all(elem in list(lineparts[i]) for elem in lettersInDigit[7]):
                lettersInDigit[3] = list(lineparts[i])
        # If it has 5 segments that all appear in the segment list for number 6, it must be 5
        for i in range(10):
            if len(lineparts[i]) == 5 and all(elem in lettersInDigit[6] for elem in list(lineparts[i])):
                lettersInDigit[5] = list(lineparts[i])
        # If it has 5 segments and isn't 3 or 5, it must be 2
        for i in range(10):
            if len(lineparts[i]) == 5 and not all(elem in list(lineparts[i]) for elem in lettersInDigit[3]) and not all(elem in list(lineparts[i]) for elem in lettersInDigit[5]):
                lettersInDigit[2] = list(lineparts[i])

        # match the last four digits from the row with what we've learned from the first 10
        numberDigits = [-1,-1,-1,-1]
        for i in range(11, 15):
            for n in range(10):
                if all(elem in list(lineparts[i]) for elem in lettersInDigit[n]) and all(elem in lettersInDigit[n] for elem in list(lineparts[i])):
                    numberDigits[i - 11] = n
        
        # convert it to a number and add it to the list
        number = (numberDigits[0] * 1000) + (numberDigits[1] * 100) + (numberDigits[2] * 10) + numberDigits[3]    
        count += number

    print("Total of all numbers: %d" % count)
