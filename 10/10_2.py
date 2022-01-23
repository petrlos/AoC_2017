#Advent of Code 2017: Day 10
def moveRight(data, currentPosition):
    currentPosition = currentPosition % len(data)
    return data[currentPosition:] + data[:currentPosition]

def oneTurn(data, lengths, currentPosition, skipSize):
    for length in lengths:
        data = moveRight(data, currentPosition) #move right
        data = list(reversed(data[:length])) + data[length:] #reverse LENGHT elements, addup the rest
        data = moveRight(data, - currentPosition) #move back left
        currentPosition += length + skipSize #correct currentPosition by length + skipsize
        skipSize += 1 #correct skipsize
    return data, currentPosition, skipSize

#Task1
lengths = [227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144]
data = list(range(256))
result, position, skipSize = oneTurn(data, lengths, 0,0)
print("Task 1:", result[0]*result[1])