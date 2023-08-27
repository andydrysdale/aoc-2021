targetMaxX = 273
targetMinX = 241
targetMaxY = -63
targetMinY = -97

hitCount = 0

for startvx in range(1000):
    for startvy in range(-1000, 1000):
        vx = startvx
        vy = startvy
        x = 0
        y = 0
        
        hitorPassedTarget = False
        while not hitorPassedTarget:
            x += vx
            y += vy 
            if vx > 0: vx -= 1
            elif vx < 0: vx =+ 1
            vy -= 1

            if x >= targetMinX and x <= targetMaxX and y >= targetMinY and y <= targetMaxY:
                hitCount += 1
                hitorPassedTarget = True
            elif x > targetMaxX or y < targetMinY: 
                hitorPassedTarget = True

print("Hitting velocity count = %d" % hitCount)

        