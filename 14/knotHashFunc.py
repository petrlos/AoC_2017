#KNOT HASH: Based on AoC 2017/Day 10

from functools import reduce
def knotHash(input):
    def oneTurn(numbers, lengths, currentPosition, skipSize):
        for length in lengths:
            numbers = moveRight(numbers, currentPosition)  # move right
            numbers = list(reversed(numbers[:length])) + numbers[length:]  # reverse LENGHT elements, addup the rest
            numbers = moveRight(numbers, - currentPosition)  # move back left
            currentPosition += length + skipSize  # correct currentPosition by length + skipsize
            skipSize += 1  # correct skipsize
        return numbers, currentPosition, skipSize

    def moveRight(numbers, currentPosition):
        currentPosition = currentPosition % len(numbers)
        return numbers[currentPosition:] + numbers[:currentPosition]

    lengths = list(map(ord, input)) + [17, 31, 73, 47, 23] #convert input to ascii + add addup sequence
    numbers, currentPosition, skipSize = list(range(256)), 0, 0 #start position
    for _ in range(64): #perform 64 runs
        numbers, currentPosition, skipSize = oneTurn(numbers, lengths, currentPosition, skipSize)
    result = ""
    for i in range(16):
        slice = numbers[i + i*15 : i*16+16]
        newChar = hex(reduce(lambda x, y: x ^ y, slice))[2:]
        result += newChar.rjust(2, "0")
    return result