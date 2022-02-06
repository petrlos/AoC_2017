#Advent of Code 2017 - Day 21
import numpy
from math import sqrt
from pprint import pprint

def stringToNumpy(string):
    string = list(map(int, string.replace("/", "").replace("#", "1").replace(".", "0")))
    size = int(sqrt(len(string)))
    numpyArray = numpy.zeros((size, size))
    for row in range(size):
        for column in range(size):
            index = size * row + column
            numpyArray[row, column] = string[index]
    return numpyArray

def decodeKey(numpyArray):
    size = numpyArray.shape[0]
    reshaped = numpy.reshape(numpyArray, (1, size ** 2))
    result = 0
    for index, number in enumerate(range(size ** 2)):
        result += reshaped[0,number] * (2 ** index)
    return result

def parseData(lines):
    rulesTwoByTwo = {}
    rulesThreeByThree = {}
    for line in lines:
        ruleKey, ruleValue = line.split(" => ")
        ruleKeyNumpy = stringToNumpy(ruleKey)
        size = ruleKeyNumpy.shape[0]
        ruleValue = stringToNumpy(ruleValue)
        for flip in range(2):
            for rotate in range(4):
                ruleKey = decodeKey(ruleKeyNumpy)
                if size == 2:
                    rulesTwoByTwo[ruleKey] = ruleValue
                elif size == 3:
                    rulesThreeByThree[ruleKey] = ruleValue
                ruleKeyNumpy = numpy.rot90(ruleKeyNumpy)
            ruleKeyNumpy = numpy.fliplr(ruleKeyNumpy)
    return rulesTwoByTwo, rulesThreeByThree

with open("test.txt") as file:
    lines = file.read().splitlines()


rulesTwoByTwo, rulesThreeByThree = parseData(lines)
pprint(rulesTwoByTwo)