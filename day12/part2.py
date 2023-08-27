def allowedToAdd(item, rte):
    if item.isupper():
        return True
    elif item == "start":
        return False
    else:
        smallCaveVisited = 0
        for i in rte:
            if i.islower() and i != "start":
                if rte.count(i) > 1: 
                    smallCaveVisited += 1 
                    
        if smallCaveVisited > 2:
            return False
        else:
            return True
                


pairs = []
routes = []
routesThatEnd = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
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
            if pair[0] == route[-1] and allowedToAdd(pair[1], route):
                    connections.append(pair[1])
            elif pair[1] == route[-1] and allowedToAdd(pair[0], route):
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
    
print("Total number of routes: ", len(routesThatEnd))
            

# routesWithoutDuplicates = []
# for elem in routesThatEnd:
#     if elem not in routesWithoutDuplicates:
#         routesWithoutDuplicates.append(elem)
# print(routesWithoutDuplicates)
# print(len(routesWithoutDuplicates))

