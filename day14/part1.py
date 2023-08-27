from collections import Counter

polymerTemplate = ""
pairInsertionRules = {}

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    polymerTemplate = file.readline()[:-1]
    
    for line in file.readlines():
        insertionRule =line[:-1].split(" -> ")
        pairInsertionRules[insertionRule[0]] = insertionRule[1]

print(polymerTemplate)
print(pairInsertionRules)

for step in range(10):
    newTemplate = polymerTemplate[0]
    for i in range(len(polymerTemplate) - 1):
        newTemplate += pairInsertionRules.get(polymerTemplate[i:i+2])
        newTemplate += polymerTemplate[i + 1]
    print("step %s, polymer=%s" % (step, newTemplate))
    polymerTemplate = newTemplate

letterCounts = Counter(polymerTemplate)

print(letterCounts)

leastFrequent = 999999999999999
mostFrequent = 0

for letter in letterCounts:
    if letterCounts[letter] < leastFrequent: leastFrequent = letterCounts[letter]
    if letterCounts[letter] > mostFrequent: mostFrequent = letterCounts[letter]

print("Difference between most frequent and least frequent counts:", mostFrequent - leastFrequent)
 
