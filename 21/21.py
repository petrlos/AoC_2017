#Advent of Code 2017 - Day 21
import numpy
from math import sqrt
from copy import deepcopy
from datetime import datetime
timestart = datetime.now()

def stringToNumpy(string): #translates string to numpy array
    string = list(map(int, string.replace("/", "").replace("#", "1").replace(".", "0")))
    size = int(sqrt(len(string)))
    numpyArray = numpy.zeros((size, size))
    for row in range(size):
        for column in range(size):
            index = size * row + column
            numpyArray[row, column] = string[index]
    return numpyArray

def decodeKey(numpyArray): #transfers numpy array to sum of (2^array index) - each array has unique key
    size = numpyArray.shape[0]
    reshaped = numpy.reshape(numpyArray, (1, size ** 2))
    result = 0
    for index, number in enumerate(range(size ** 2)):
        result += reshaped[0,number] * (2 ** index)
    return result

def parseData(lines):
    #each rule is saved to dictionary inkl. rotation + flip -> up to 8 times
    #not necessary to search and rotate during iterations of main cycle
    rulesTwoByTwo = {}
    rulesThreeByThree = {}
    for line in lines:
        ruleKey, ruleValue = line.split(" => ")
        ruleKeyNumpy = stringToNumpy(ruleKey)
        size = ruleKeyNumpy.shape[0]
        ruleValue = stringToNumpy(ruleValue)
        for flip in range(2): #flip
            for rotate in range(4): #rotate 4 times
                ruleKey = decodeKey(ruleKeyNumpy)
                if size == 2: #each key-size has separate dict
                    rulesTwoByTwo[ruleKey] = ruleValue
                elif size == 3:
                    rulesThreeByThree[ruleKey] = ruleValue
                ruleKeyNumpy = numpy.rot90(ruleKeyNumpy)
            ruleKeyNumpy = numpy.fliplr(ruleKeyNumpy)
    return rulesTwoByTwo, rulesThreeByThree

def slice(grid, topLeft, step): #cuts of grid 2x2 resp. 3x3
    row, column = topLeft
    if step == 3:
        cutOfRows = grid[[row, row + 1, row + 2], :]
        cutOfColumns = cutOfRows[:, [column, column + 1, column + 2]]
    else:
        cutOfRows = grid[[row, row + 1], :]
        cutOfColumns = cutOfRows[:, [column, column + 1]]
    return cutOfColumns

def performNSteps(steps, grid):
    for _ in range(steps):
        gridSize = grid.shape[0]
        transferDict = rulesThreeByThree #default dictionary is size 3, only if it is not :) see line 61
        gridStep = 3
        newGridSize = gridSize // 3 * 4
        if gridSize % 2 == 0: #if dividible by to - dictionary size is 2
            transferDict = rulesTwoByTwo
            gridStep = 2
            newGridSize = gridSize // 2 * 3
        row, col = 0, 0
        newGrid = numpy.zeros((newGridSize, newGridSize)) #create new grid full of zeros
        for _ in range((gridSize // gridStep) ** 2):
            cutOf = slice(grid, (row, col), gridStep) #slice old grid
            toBeInserted = transferDict[decodeKey(cutOf)] #get new key
            offSet = gridStep + 1
            for x in range(gridStep + 1): #copy to new grid
                for y in range(gridStep + 1):
                    newGrid[x + (row // gridStep) * offSet, y + (col // gridStep) * offSet] = toBeInserted[x, y]
            col += gridStep #move to next column
            if col >= gridSize: #if column out, move to next row + first column
                col = 0
                row += gridStep
        grid = deepcopy(newGrid) #copy grid
    return int(newGrid.sum())

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
rulesTwoByTwo, rulesThreeByThree = parseData(lines)

#start grid
grid = numpy.array([[0,1,0], [0,0,1], [1,1,1]])

print("Task 1:",performNSteps(5, grid))
print("Runtime Task1:", datetime.now() - timestart)
timestart = datetime.now()
print("Task 2:",performNSteps(18, grid))
print("Runtime Task2:", datetime.now() - timestart)