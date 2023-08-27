algorithm = ""
inputImage = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    algorithm = file.readline()[:-1]
    for line in file.readlines():
        inputImage.append(line[:-1]) 

print(inputImage)

def getPixel(x, y, default):
    if x < 0 or y < 0 or x >= len(inputImage[0]) or y >= len(inputImage):
        return default
    else:
        return inputImage[y][x]


for iteration in range(50):
    defaultChar = "."
    if iteration % 2 == 1 and algorithm[0] == "#": defaultChar = "#"

    outputImage = []
    
    for y in range(-1, len(inputImage) + 1):
        newRow = ""
        for x in range(-1, len(inputImage[0]) + 1):
            binaryString = ""
            for j in range(-1, 2):
                for i in range(-1, 2):
                    if getPixel(x + i, y + j, defaultChar) == "#": 
                        binaryString += "1"
                    else: 
                        binaryString += "0"
            newRow += algorithm[int(binaryString, 2)]
        outputImage.append(newRow)

    noOfLightPixels = len("".join(outputImage).replace(".", ""))
    print("Count after %d iterations: %d" % (iteration + 1, noOfLightPixels))
    
    inputImage = outputImage.copy()
    


              

