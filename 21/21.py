#Advent of Code 2017 - Day 21
import numpy

def stringToNumpy(string):
    string = string.replace("/", "").replace("#", "1").replace(".", "0")
    string = list(map(int, string))
    sizes = {4: (2,2), 9:(3,3), 16:(4,4)}
    numpyArray = numpy.zeros(sizes[len(string)])
    size = sizes[len(string)][0]
    for row in range(size):
        for column in range(size):
            index = size * row + column
            numpyArray[row, column] = string[index]
    return numpyArray

def parseData(lines):
    rulesTwoByTwo = {}
    rulesThreeByThree = {}
    for line in lines:
        ruleKey, ruleValue = line.split(" => ")
        ruleKeyNumpy = stringToNumpy(ruleKey)
        for flip in range(2):
            for rotate in range(4):
                ...
    return rulesTwoByTwo, rulesThreeByThree

with open("test.txt") as file:
    lines = file.read().splitlines()


rulesTwoByTwo, rulesThreeByThree = parseData(lines)