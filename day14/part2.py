import time
from collections import Counter

#polymerTemplate = []
pairInsertionRules = {}

with open("testdata.txt", "r", encoding="utf-8") as file:
    polymerTemplate = list(file.readline()[:-1])
    print(polymerTemplate)
    for line in file.readlines():
        insertionRule =line[:-1].split(" -> ")
        pairInsertionRules[insertionRule[0]] = insertionRule[1]

length = len(polymerTemplate)
for iteration in range(40):
    startTime = time.perf_counter()
    for x in range(1, length, 2):
        polymerTemplate.insert(x, (pairInsertionRules[polymerTemplate[x-1] + polymerTemplate[x]]))
    length = (length * 2) - 1
    elapsedTimeString = time.perf_counter() - startTime
    print("iteration = %d, length = %d, time = %ds" % (iteration, length, elapsedTimeString))

letterCounts = Counter(polymerTemplate)

print(letterCounts)

leastFrequent = 999999999999999
mostFrequent = 0

for letter in letterCounts:
    if letterCounts[letter] < leastFrequent: leastFrequent = letterCounts[letter]
    if letterCounts[letter] > mostFrequent: mostFrequent = letterCounts[letter]

print("Difference between most frequent and least frequent counts:", mostFrequent - leastFrequent)
 
