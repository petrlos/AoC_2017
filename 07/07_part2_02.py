#Advent of Code 2017: Day 7
from pprint import pprint

def parseData(lines):
    tree = dict()
    for line in lines:
        helpDict = dict()
        if " -> " in line:
            front, back = line.split(" -> ")
            parent, value = front.split(" ")
            kids = back.split(", ")
            done = False
        else:
            parent, value = line.split(" ")
            kids = None
            done = True
        helpDict["value"] = int(value[1:-1])
        helpDict["kids"] = kids
        helpDict["done"] = done
        tree[parent] = helpDict
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

