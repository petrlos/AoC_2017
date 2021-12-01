#Advent of Code 2017: Day 9

def task1(data):
    data = data.replace("!!", "")
    checkSum = []; nesting = 0
    garbagge = False
    for index in range(len(data)):
        if data[index - 1] != "!":
            if data[index] == "<":
                garbagge = True
            if data[index] == ">":
                garbagge = False
            if not garbagge:
                if data[index] == "{":
                    nesting += 1
                if data[index] == "}":
                    checkSum.append(nesting)
                    nesting -= 1
    return sum(checkSum)

def task2(data):
    index = 0; counter = 0
    counterOn = False
    while index < len(data)-1:
        if data[index] == "!":
            index += 1
        else:
            if counterOn and data[index] != "":
                counter += 1
            if data[index] == "<":
                counterOn = True
            if data[index] == ">":
                counterOn = False
        index += 1
    return counter

with open("data.txt", "r") as file:
    data = file.read()

print("Task 1:",task1(data))

#TODO: Task 2 not working - vraci spatne cislo, netusim proc
print("Task 2:",task2(data))
