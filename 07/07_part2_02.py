#Advent of Code 2017: Day 7
from collections import Counter

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

def kidsCompleted(parent):
    kids = tree[parent]["kids"]
    for kid in kids:
        if not tree[kid]["done"]:
            return False
    return True

def countTree(tree):
    done = False
    while not done:
        done = True
        for parent in tree.keys():
            if not tree[parent]["done"]:
                if kidsCompleted(parent):
                    kids = tree[parent]["kids"]
                    for kid in kids:
                        tree[parent]["value"] += tree[kid]["value"]
                    tree[parent]["done"] = True
                done = False
    return tree

def findDefectParent(startKey):
    defektKey = startKey
    defectKeyFound = False
    result = 0
    while not defectKeyFound:
        values = [tree[parent]["value"] for parent in tree[defektKey]["kids"]]
        if len(set(values)) > 1:
            defectValue = Counter(values).most_common()[-1][0]
            difference = Counter(values).most_common()[-1][0] - Counter(values).most_common()[0][0]
            for parent in tree[defektKey]["kids"]:
                if tree[parent]["value"] == defectValue:
                    defektKey = parent
        else:
            result = tree[defektKey]["value"] - difference
            for kid in tree[defektKey]["kids"]:
                result -= tree[kid]["value"]
            defectKeyFound = True


    return defektKey, result

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

tree = parseData(lines)

#Task1:
startKey = findTopParent(lines)
print("Task1:", startKey)
tree = countTree(tree)

#Task2:
defectKey, defectParentValue = findDefectParent(startKey)
print("Task2: defect key {0} should have value: {1}".format(defectKey, defectParentValue))