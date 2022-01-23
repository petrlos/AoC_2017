#Advent of Code 2017: Day 10
from functools import reduce
from datetime import datetime
timeStart = datetime.now()

def moveRight(numbers, currentPosition):
    currentPosition = currentPosition % len(numbers)
    return numbers[currentPosition:] + numbers[:currentPosition]

def oneTurn(numbers, lengths, currentPosition, skipSize):
    for length in lengths:
        numbers = moveRight(numbers, currentPosition) #move right
        numbers = list(reversed(numbers[:length])) + numbers[length:] #reverse LENGHT elements, addup the rest
        numbers = moveRight(numbers, - currentPosition) #move back left
        currentPosition += length + skipSize #correct currentPosition by length + skipsize
        skipSize += 1 #correct skipsize
    return numbers, currentPosition, skipSize

def knotHash(input):
    lengths = list(map(ord, input)) + [17, 31, 73, 47, 23] #convert input to ascii + add addup sequence
    numbers, currentPosition, skipSize = list(range(256)), 0, 0 #start position
    for _ in range(64): #perform 64 runs
        numbers, currentPosition, skipSize = oneTurn(numbers, lengths, currentPosition, skipSize)
    result = ""
    for i in range(16):
        slice = numbers[i + i*15 : i*16+16]
        result += hex(reduce(lambda x, y: x ^ y, slice))[2:]
    return result

#Task1
lengths = [227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144]
numbers = list(range(256))
result, position, skipSize = oneTurn(numbers, lengths, 0,0)
print("Task 1:", result[0]*result[1])

#Task2
input = "227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144"
print("Task 2:", knotHash(input))
print("Runtime:", datetime.now() - timeStart)