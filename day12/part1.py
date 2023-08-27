pairs = []
routes = []
routesThatEnd = []

with open("testdata3.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file.readlines():
        pairs.append(line[:-1].split("-"))
 
routes.append(["start"]) 

iterationCount = 0
routesFound = True

while(routesFound):
    routesFound = False
    iterationCount += 1
    
    routesCopy = routes.copy()
    for route in routesCopy:
        connections = []

        for pair in pairs:
            if pair[0] == route[-1]:
                if pair[1].isupper() or (pair[1].islower() and pair[1] not in route): 
                    connections.append(pair[1])
            elif pair[1] == route[-1]:
                if pair[0].isupper() or (pair[0].islower() and pair[0] not in route): 
                    connections.append(pair[0])
        for connection in connections:
            newRoute = route.copy()
            newRoute.append(connection)
            if connection == "end":
                if newRoute not in routesThatEnd:
                    routesThatEnd.append(newRoute)
                    routesFound = True 
            else:
                if newRoute not in routes:
                    routes.append(newRoute)
                    routesFound = True
    print("iteration = %d, complete routes found = %d" % (iterationCount, len(routesThatEnd)))
    
print(routesThatEnd)
print(len(routesThatEnd))
            

