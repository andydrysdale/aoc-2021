with open("puzzledata.txt", "r", encoding="utf-8") as file:
    horizontal = 0
    depth = 0
    
    for line in file.readlines():
        lineparts = line.split()
        
        if(lineparts[0] == "forward"):
            horizontal += int(lineparts[1])
        elif(lineparts[0] == "up"):
            depth -= int(lineparts[1])
        elif(lineparts[0] == "down"):
            depth += int(lineparts[1])
    
    print("horizontal: %d" % horizontal)
    print("     depth: %d" % depth)
    print("   product: %d" % (horizontal * depth))

