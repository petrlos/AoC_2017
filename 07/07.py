#Advent of Code 2017 - Day 7 - Task1

import re
regName = re.compile(r"\w+")

with open("data.txt", "r") as file:
    lines = file.read().replace(" -> ",":").splitlines()

#Define dictionary of Adresses
adresses = {}
for line in lines:
    if ":" in line:
        adress = line.split(":")
        adresses.setdefault(adress[0], adress[1])
    else:
        adresses.setdefault(line, "")

for key in adresses.keys():
    keyName = regName.search(key).group()
    if keyName not in " ".join(adresses.values()):
        result = key


print("Task 1:", result)