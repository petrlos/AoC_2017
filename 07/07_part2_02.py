#Advent of Code 2017: Day 7
import re

def parseData(lines):
    tree = []
    for line in lines:
        ...
    return tree

def findTopParent(lines):
    kids = []
    parents = []
    for line in lines:
        if " -> " in line:
            parent, kid = line.split(" -> ")
            parents.append(parent.split(" ")[0])
            kids += kid.split(", ")
        else:
            parents.append(line.split(" ")[0])
    return list(set(parents) - set(kids))[0]

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

tree = parseData(lines)
startKey = findTopParent(lines)
print(startKey)