#Advent of Code 2017 - Day 12

def searchNodes(start):
    #zapise vstup do slovniku a vyhleda s nim spojene programy
    connections.setdefault(start)
    for key in nodesDict[start]:
        #ochrana pred spadnutim do nekonecne rekurze - pokud key jeste neexistuje, overi se jeho koreny
        if key not in connections.keys():
            searchNodes(key)

with open("data.txt", "r") as file:
    nodes = file.read().replace(" <-> ", ":").splitlines()

#zakladni slovnik ve formatu koren: [kam miri]
nodesDict = {}
for node in nodes:
    dictEntry = node.split(":")
    nodesDict.setdefault(dictEntry[0], dictEntry[1].split(", "))

#Task 1:
connections = {}
#projde veskere spojeni pro koren "0"
searchNodes("0")
print("Task 1:",len(connections))

#Task 2:
groupsCount = 0
#pomocna promenna na task2: ktere koreny jeste neprosel - musi byt str, zakladni slovnik je taky str
possibleNodes = [str(x) for x in range(0,len(nodes))]

#vyhleda spojeni pro 1. neprohledany koren v possible nodes, po provereni vymazene nalezene koreny ze seznamu
while len(possibleNodes) > 0:
    connections = {}
    searchNodes(str(possibleNodes[0]))
    for itemFound in connections.keys():
        possibleNodes.remove(itemFound)
    groupsCount += 1

print("Task 2:",groupsCount)
