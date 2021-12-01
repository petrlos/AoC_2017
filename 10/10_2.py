#Advent of Code 2017: Day 10

from collections import deque

def oneTurn(data, currentPosition, length, skipsize):
    #posune list, aby currentPosition byla na 0
    shiftedData = data[currentPosition:] + data[:currentPosition]
    #otoci prvnich "length" pozic + pripoji zbytek retezce
    shiftedRotatedData = list(reversed(shiftedData[:length])) + shiftedData[length:]
    #posune nazpet
    if currentPosition > 0:
        newData = shiftedRotatedData[currentPosition-1:] + shiftedRotatedData[:currentPosition-1]
    else:
        newData = shiftedRotatedData
    position = (currentPosition + skipsize + length) % len(data)
    print(newData)
    return position, newData


#MAIN

lengths = [3,4,1,5]
position = 0
data = [0,1,2,3,4]

for skipsize, length in enumerate(lengths):
    position, data = oneTurn(data, position, length, skipsize)
