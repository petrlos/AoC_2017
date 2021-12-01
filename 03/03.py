#Advent of Code 20167 - Day 03
#Task 1 counted using excel+paper: result 430

def getNeighboursSum(midPoint):
    neighboursSum = 0
    for neighbour in neighbours:
        coordToCountIn = tuple(map(lambda x, y: x + y, midPoint, neighbour))
        if coordToCountIn in spiral.keys():
            neighboursSum += spiral[coordToCountIn]
    #if something larger than searched number found, save it
    if neighboursSum > searchedNumber:
        result.append(neighboursSum)
    return neighboursSum

#up, left, down, right
moveDirect = [(0,1,),(-1,0), (0,-1), (1,0)]
neighbours = [(-1,1), (0,1), (1,1) ,(-1,0) ,(1,0) ,(-1,-1), (0,-1), (1,-1)]

#input spiral - first two values
spiral = {(0,0): 1, (1,0): 1 }

direction = 0 #default direction is up
steps = 1 #size of the first square is 1
lastNumber = (1, 0) #last input in spiral

searchedNumber = 312051

result = []

#to move in spiral:
#go up by (2x steps - 1), left by (2x steps), down by (2x steps), right by (2x steps + 1) und turn up
#repeat :)

while True:
    for _ in range(0, 2*steps-1):
        newNumber = tuple(map(lambda x, y: x + y, lastNumber, moveDirect[direction]))
        neighboursSum = getNeighboursSum(newNumber)
        spiral.setdefault(newNumber, neighboursSum)
        lastNumber = newNumber
    direction += 1
    for _ in range(0,2):
        for _ in range(0, 2*steps):
            newNumber = tuple(map(lambda x, y: x + y, lastNumber, moveDirect[direction]))
            neighboursSum = getNeighboursSum(newNumber)
            spiral.setdefault(newNumber, neighboursSum)
            lastNumber = newNumber
        direction += 1
    for _ in range(0, 2*steps + 1):
        newNumber = tuple(map(lambda x, y: x + y, lastNumber, moveDirect[direction]))
        neighboursSum = getNeighboursSum(newNumber)
        spiral.setdefault(newNumber, neighboursSum)
        lastNumber = newNumber
    direction = 0
    steps += 1
    if neighboursSum > searchedNumber:
        break

#print the smallest number from larger ones
print("Task 2:",min(result))