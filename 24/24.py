#Advent of Code 2017: Day 24
from copy import deepcopy
from random import randrange
from datetime import datetime
start = datetime.now()

#Brute Force - not working: 100.000 iterations took about 11 minutes, incorrect :D

def somethingToConnect(currentEnd):
    for cableLeft in cablesLeft:
        if currentEnd in cableLeft:
            return True
    return False

def getNewCable(currentEnd, length):
    newConnector = []
    readyToConnect = False
    while not readyToConnect:
        newIndex = randrange(length)
        if currentEnd in cablesLeft[newIndex]:
            readyToConnect = True
            newConnector = cablesLeft[newIndex]
    if newConnector[0] == currentEnd:
        newEnd = newConnector[1]
    else:
        newEnd = newConnector[0]
    return newConnector, newEnd

#MAIN:

with open("data.txt") as file:
    connectors = [x.split("/") for x in file.read().splitlines()]

possibleConnections = []

maxStrength = 0
for connector in connectors:
    maxStrength += int(connector[0]) + int(connector[1])
print("Max strength:",maxStrength)

iterrations = 100

for done in range(iterrations):
    for begin in connectors:
        cablesLeft = deepcopy(connectors)
        if "0" in begin:
            currentCable = []
            currentCable.append(begin)
            cablesLeft.remove(begin)
            if begin[0] == "0":
                currentEnd = begin[1]
            else:
                currentEnd = begin[0]
            while somethingToConnect(currentEnd):
                newConnector, currentEnd = getNewCable(currentEnd, len(cablesLeft))
                currentCable.append(newConnector)
                cablesLeft.remove(newConnector)
            if currentCable not in possibleConnections:
                possibleConnections.append(currentCable)
    if done % 1000 == 0:
        print(done)

lengths, strengths = [], []
for cable in possibleConnections:
    lengths.append(len(cable))
    strength = 0
    for member in cable:
        strength += int(member[0]) + int(member[1])
    strengths.append(strength)

print("Possible connections found:", len(possibleConnections))
print("Max length:",max(lengths))
print("Max strength:",max(strengths))
print("Runtime for {0} iterrations:".format(iterrations), datetime.now()-start)