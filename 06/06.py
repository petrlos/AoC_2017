#Advent of Code 2017 Day 6
def rearange(dataBank):
    startIndex = dataBank.index(max(dataBank))
    rearangeCount = dataBank[startIndex]
    dataBank[startIndex] = 0
    while rearangeCount > 0:
        rearangeCount -= 1
        startIndex += 1
        if startIndex > len(dataBank) - 1:
            startIndex = 0
        dataBank[startIndex] += 1
    return dataBank

#MAIN
with open("data.txt", "r") as file:
    dataBank = [int(x) for x in file.read().split("\t")]

didSeeBefore = []
didSeeBefore.append(dataBank * 1)

while True:
    newCombination = rearange(dataBank)
    if newCombination not in didSeeBefore:
        didSeeBefore.append(newCombination * 1)
    else:
        break

task2 = len(didSeeBefore) - didSeeBefore.index(newCombination)

print("Task 1:",len(didSeeBefore))
print("Task 2:", task2)