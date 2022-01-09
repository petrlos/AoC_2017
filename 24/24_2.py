#Advent of Code 2017 Day 24
import re
from collections import deque

class Cable:
    def __init__ (self, components, end):
        self.components = components
        self.end = end

def parseData(lines):
    cables = []
    for line in lines:
        begin, end = list(map(int, regNum.findall(line)))
        cables.append([begin, end])
    return cables

#MAIN
regNum = re.compile(r"\d+")

with open("data.txt") as file:
    lines = file.read().splitlines()

components = parseData(lines)
queue = deque()

for component in components:
    if 0 in component:
        newCable = Cable([component], component[1])
        queue.append(newCable)

done = []
while queue:
    currentCable = queue[0]
    notconnected = False
    for component in components:
        if currentCable.end in component and component not in currentCable.components:
            notconnected = True
            newComponents = currentCable.components + [component]
            if currentCable.end == component[0]:
                newEnd = component[1]
            else:
                newEnd = component[0]
            queue.append(Cable(newComponents, newEnd))
    if not notconnected:
        done.append(currentCable.components)
    queue.popleft()

done = sorted(done, key = len)
maxLength = len(done[-1])
strengthsTask1 = []
strengthsTask2 = []
for cable in done:
    strength = sum( sum(x) if isinstance(x, list) else x for x in cable )
    strengthsTask1.append(strength)
    if len(cable) == maxLength:
        strengthsTask2.append(strength)

print("Task 1:",max(strengthsTask1))
print("Task 2:",max(strengthsTask2))
