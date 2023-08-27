#target area: x=217..240, y=-126..-69
targetMaxX = 240
targetMinX = 217
targetMaxY = -69
targetMinY = -126

maxY = -999999999

for startvx in range(100):
    for startvy in range(-100, 100):
        vx = startvx
        vy = startvy
        x = 0
        y = 0
        iterationMaxY = -999999999
        
        passedTarget = False
        while not passedTarget:
            x += vx
            y += vy 
            if vx > 0: vx -= 1
            elif vx < 0: vx =+ 1
            vy -= 1

            if y > iterationMaxY: iterationMaxY = y
            if x >= targetMinX and x <= targetMaxX and y >= targetMinY and y <= targetMaxY:
                if iterationMaxY > maxY: maxY = iterationMaxY
            elif x > targetMaxX or y < targetMinY: 
                passedTarget = True

print("Max Y = %d" % maxY)

        