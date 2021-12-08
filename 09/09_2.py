#Advent of Code 2021 Day 9: Vs. 2

def checkData(line):
    groupsCounter = 0
    index = 0
    groupDepth = 0
    garbage = False
    garbageCounter = 0
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
                else:
                    garbageCounter += 1
        index += 1
    return groupsCounter, garbageCounter

#MAIN
with open("data.txt") as file:
    data = file.read().splitlines()

for line in data:
    task1, task2 = checkData(line)

print("Task 1:", task1)
print("Task 2:", task2)