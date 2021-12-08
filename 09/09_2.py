#Advent of Code 2021 Day 9: Vs. 2

def checkData(line):
    groupsCounter = 0
    index = 0
    groupDepth = 0
    garbage = False # if true, no garbage
    while index < len(line):
        ignoreNext = False
        if line[index] == "!":
            ignoreNext = True
        if not garbage:
            if line[index] == "{":
                groupDepth += 1
                groupsCounter += groupDepth
            elif line[index] == "}":
                groupDepth -= 1
            elif line[index] == "<":
                garbage = True
        else:
            if ignoreNext:
                index += 1
            else:
                if line[index] == ">":
                    garbage = False
        index += 1

    return groupsCounter


with open("data.txt") as file:
    data = file.read().splitlines()

for line in data:
    print(checkData(line))
