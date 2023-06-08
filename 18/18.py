#Advent of Code 2017 - Day 18
def decodeLine(parameter):
    if parameter.isalpha():
        result = registers[parameter]
    else:
        result = int(parameter)
    return result

with open("test.txt") as file:
    lines = file.read().splitlines()

registers = {}; sound = 0; currentLine = 0 ; rcv = 0

while rcv == 0:
    line = lines[currentLine]
    where = line[4]
    if where not in registers.keys():
        registers.setdefault(where, 0)
    if "snd" in line:
        sound = registers[where]
    elif "add" in line:
        registers[where] += decodeLine(line[6:])
    elif "set" in line:
        registers[where] = decodeLine(line[6:])
    elif "mul" in line:
        registers[where] *= decodeLine(line[6:])
    elif "mod" in line:
        registers[where] %= decodeLine(line[6:])
    elif "rcv" in line:
        if decodeLine(where) != 0:
            rcv = sound
    elif "jgz" in line:
        if decodeLine(where) > 0:
            currentLine += decodeLine(line[6:]) -1 #musim odecist 1, na dalsim radku se jedna pricte
    currentLine += 1

print("Task 1:", rcv)