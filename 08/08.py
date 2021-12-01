#Advent of Code 2017: Day 8
import re

def performAction(where):
    if "inc" in where:
        return 1
    elif "dec" in where:
        return -1

regWord = re.compile(r"\w+")
regNum = re.compile(r"(-)?\d+")

with open("data.txt", "r") as file:
    instructions = file.read().replace(" if ",":").splitlines()

numbers = {}
task2 = []

for instruction in instructions:
    instructionSplit = instruction.split(":")
    where = instructionSplit[0]; cond = instructionSplit[1]
    condVar = regWord.search(cond).group(); condValue = int(regNum.search(cond).group())
    newNumberVar = regWord.search(where).group(); newNumberValue = int(regNum.search(where).group())
    numbers.setdefault(condVar, 0); numbers.setdefault(newNumberVar, 0)
    if "> " in cond:
        if numbers[condVar] > condValue:
            numbers[newNumberVar] = numbers[newNumberVar] + (newNumberValue) * performAction(where)
    elif "< " in cond:
        if numbers[condVar] < condValue:
            numbers[newNumberVar] = numbers[newNumberVar] + (newNumberValue) * performAction(where)
    elif "==" in cond:
        if numbers[condVar] == condValue:
            numbers[newNumberVar] = numbers[newNumberVar] + (newNumberValue) * performAction(where)
    elif ">=" in cond:
        if numbers[condVar] >= condValue:
            numbers[newNumberVar] = numbers[newNumberVar] + (newNumberValue) * performAction(where)
    elif "<=" in cond:
        if numbers[condVar] <= condValue:
            numbers[newNumberVar] = numbers[newNumberVar] + (newNumberValue) * performAction(where)
    elif "!=" in cond:
        if numbers[condVar] != condValue:
            numbers[newNumberVar] = numbers[newNumberVar] + (newNumberValue) * performAction(where)
    else:
        print("INVALID INSTRUCTION")
    task2.append(max(numbers.values()))

print("Task1:",max(numbers.values()))
print("Task2:",max(task2))