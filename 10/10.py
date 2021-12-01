#Advent of Code 2017 - Day 10
from functools import reduce

def performOneTurn(lengths, numbers, currentPosition=0, skipSize=0):
    #input data:

    for length in lengths:
        cutOff = []
        index = currentPosition
        #vytahne z listu numbers vyrez o delce length, nezavisle na tom, kde zacina
        while len(cutOff) < length:
            index %= len(numbers)
            cutOff.append(numbers[index])
            index += 1
        rest = []
        #vytahne z listu numbers zbyvajici cisla
        while len(cutOff) + len(rest) < len(numbers):
            index %= len(numbers)
            rest.append(numbers[index])
            index += 1
        #obrati list cutoff + prevede na list
        cutOff = list(reversed(cutOff))
        #napoji zbyvajici cisla v rest za cutoff
        for number in rest:
            cutOff.append(number)
        index = currentPosition
        #projde vsechny cisla v cutoff a prepise jimi cisla v numbers od current positin
        for number in cutOff:
            numbers[index] = number
            index += 1
            index %= len(numbers)
        #currentposition navysi o length a skipsize
        currentPosition += length + skipSize
        skipSize += 1
        currentPosition %= len(numbers)
    return numbers, currentPosition, skipSize

#MAIN

input = [int(x) for x in "227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144".split(",")]
task1result, a, b = performOneTurn(input, list(range(256)))
print("Task1:",task1result[0]*task1result[1])

input = ""

#TODO: Knot hash task2 - nevim proc a jak

addUpSequence = [17,31,73,47,23]
inputSequence = [ord(x) for x in input]

lengths = inputSequence + addUpSequence
#print(lengths)

numbers = list(range(255))
skipSize = 0; currentPosition = 0
for _ in range(64):
    numbers, currentPosition, skipSize = performOneTurn(lengths, numbers, currentPosition, skipSize)

#spare hash to dense hash:
result = []
for i in range(0,16):
    #vybere vyrez z numbers o delce 16 znaku
    cutOff = numbers[i*16:(i*16)+16]
    #spocita XOR z vyrezu a prevede ho na HEX ve formatu 00 --> FF
    result.append(format(reduce(lambda x, y: x ^ y, cutOff), "03x")[1:])
print("incorrect Task 2:","".join(result))
