#Advent of Code 2017 - Day 16
import re
from collections import deque

def performDance(instructions, programs):
    #posunu deque o spinBy smerem doleva
    def spin(programs, spinBy):
        for _ in range(0,spinBy):
            programs.appendleft(programs[-1])
            programs.pop()
        return programs

    # prohodi znaky na pozici [indexes]
    def exchangePrograms(programs, indexes):
        programs[indexes[0]], programs[indexes[1]] = programs[indexes[1]], programs[indexes[0]]
        return programs

    # prohodi volane znaky - zjisti jejich indexy, pak zavola funkci prohod indexy
    def partnerPrograms(programs, partners):
        index1 = programs.index(partners[0])
        index2 = programs.index(partners[1])
        exchangePrograms(programs, [index1, index2])
        return programs

    for line in instructions:
        if line[0] == "s":
            programs = spin(programs, int(regNum.search(line).group()))
        elif line[0] == "x":
            indexes = [int(x) for x in regNum.findall(line)]
            programs = exchangePrograms(programs, indexes)
        elif line[0] == "p":
            programs = partnerPrograms(programs, line[1:].split("/"))
        else:
            print("INVALID INSTRUCTION")
    return programs

#MAIN
regNum = re.compile(r"\d+")

with open("data.txt", "r") as file:
    instructions = file.read().split(",")

start = "abcdefghijklmnop"

#Task 1 - provede 1 otocku
programs = deque(start)
task1 = performDance(instructions, programs) * 1
print("".join(task1))

#Task 2 - provede  indexNeeded otocek
print("Task 2")
indexNeeded = 1000000000
oneCycle = 0 # jeden cyklus - po provedeni oneCycle otocek je vysledek opet "abcd.. nop"
while True:
    performDance(instructions, programs)
    oneCycle += 1
    if programs == deque(start):
        break

#k poctu cyklu se musi pricist jednicka - na navrat na 1. pzici nasledujiciho kola je potreba n+1 otocek
dancesNeeded = indexNeeded % (oneCycle + 1)
print(dancesNeeded)

programs = deque(start) * 1
for _ in range(0,dancesNeeded):
    programs = performDance(instructions, programs)
print("Task2 % result:","".join(programs))

#kontrola pro mala cisla:
"""
programs = deque(start) * 1
result = []
for _ in range(0,indexNeeded):
    programs = performDance(instructions, programs)
    result.append(programs*1)

print("Task2 control: ","".join(result[-1]))
"""