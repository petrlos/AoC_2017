#Advent of Code 2017 - Day 7
import re
from pprint import pprint as pp

test = False
if test:
    file = "test.txt"
    startKey = "tknk"
else:
    file = "data.txt"
    startKey = "hlhomy"

def sumWithRecursion(key):
    parent = tree[key]
    for childKey in parent["kids"]:
        child = tree[childKey] #childKey = key, child = value
        if child["counted"] == False:
            sumWithRecursion(childKey)
        else:
            parent["weight"] += child["weight"]
            parent["counted"] = True

regName = re.compile(r"[a-z]+")
regNum = re.compile(r"\d+")

with open(file, "r") as file:
    lines = file.read().replace(" -> ",":").splitlines()

#definice stromu
tree = {}
for line in lines:
    helpDict = {}
    weight = int(regNum.search(line).group())
    discs = regName.findall(line)
    if len(discs) > 1:
        helpDict.setdefault("kids", discs[1:])
        helpDict.setdefault("weight", weight)
        helpDict.setdefault("counted", False)
    else:
        helpDict.setdefault("weight", weight)
        helpDict.setdefault("counted", True)
    tree.setdefault(discs[0], helpDict)

while tree[startKey]["counted"] == False:
    sumWithRecursion(startKey)

#pp(tree)
# TODO: vyvazeny strom, nepocita spravne

print(startKey, tree[startKey])

for kid in tree[startKey]["kids"]:
    print(tree[kid]["weight"])
