#Advent of Code 2017 - Day 23
import re

def decodeLine(parameter):
    if parameter.isalpha():
        result = registers[parameter]
    else:
        result = int(parameter)
    return result

#MAIN:
with open("data.txt", "r") as file:
    instructions = file.read().splitlines()

registers = {"a":1, "h":0}

currentLine = 0
mulCounter = 0
while True:
    line = instructions[currentLine]
    where = line[4]
    what = decodeLine(line[6:])
    if where not in registers.keys():
        registers.setdefault(where, 0)
    if "set" in line:
        registers[where] = what
    elif "sub" in line:
        registers[where] -= what
    elif "mul" in line:
        mulCounter += 1
        registers[where] *= what
    elif "jnz" in line: # "JNZ X Y" - triggers only, if X != 0
        where = decodeLine(where)
        if where != 0:
            currentLine += what -1
    print(registers["h"])
    currentLine += 1
    if currentLine >= len(instructions):
        break
print(mulCounter)
print(registers)

#TODO: Optimalizace programu