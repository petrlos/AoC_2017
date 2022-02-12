#Advent of Code 2017: Day 7
from collections import Counter

def parseData(lines):
    tree = dict()
    for line in lines:
        helpDict = dict()
        if " -> " in line: #node with kids
            front, back = line.split(" -> ")
            parent, value = front.split(" ")
            kids = back.split(", ")
            done = False
        else: #node without kids
            parent, value = line.split(" ")
            kids = None
            done = True #no kids = no counting needed
        helpDict["value"] = int(value[1:-1])
        helpDict["kids"] = kids
        helpDict["done"] = done
        tree[parent] = helpDict
    return tree

def findTopParent(lines): #find parent, which does not appear as a kid anywhere - set difference
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
                if kidsCompleted(parent): #if all kids completed
                    kids = tree[parent]["kids"]
                    for kid in kids:
                        tree[parent]["value"] += tree[kid]["value"] #add up value of all kids
                    tree[parent]["done"] = True
                done = False #make sure all parents are counted
    return tree

def findDefectParent(startKey):
    defektKey = startKey
    defectKeyFound = False #repeat until result found
    result, difference = 0, 0
    while not defectKeyFound:
        values = [tree[parent]["value"] for parent in tree[defektKey]["kids"]] #list of values of current parent
        if len(set(values)) > 1: #two different
            defectValue = Counter(values).most_common()[-1][0] #the least common should be corrected
            difference = Counter(values).most_common()[-1][0] - Counter(values).most_common()[0][0]
            for parent in tree[defektKey]["kids"]: #find key with defect value and repeat
                if tree[parent]["value"] == defectValue:
                    defektKey = parent
        else:
            result = tree[defektKey]["value"] - difference #subtract difference
            for kid in tree[defektKey]["kids"]:
                result -= tree[kid]["value"] #subract kids values
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