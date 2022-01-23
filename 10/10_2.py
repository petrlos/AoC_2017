#Advent of Code 2017: Day 10
from collections import deque
def moveRight(data, currentPosition):
    currentPosition = currentPosition % len(data)
    return data[currentPosition:] + data[:currentPosition]

def oneTurn(data, lengths, currentPosition, skipSize):
    for length in lengths:
        data = moveRight(data, currentPosition)
        data = list(reversed(data[:length])) + data[length:]
        data = moveRight(data, - currentPosition)
        currentPosition += length + skipSize
        skipSize += 1
    return data

#MAIN

lengths = [227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144]
position = 0
data = list(range(256))

#Task1
result = oneTurn(data, lengths, 0,0)[:2]
print("Task 1:", result[0]*result[1])