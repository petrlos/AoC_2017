#Advent of Code 2017: Day 25
import re
def defineStates(lines):
    states = {}
    regStart = re.compile(r"Begin in state ([A-Z])")
    regSteps = re.compile(r"Perform a diagnostic checksum after (\d*) steps.")
    regState = re.compile(r"In state ([A-Z]):")
    regValue = re.compile(r"If the current value is (\d):")
    regWrite = re.compile(r"Write the value (\d)")
    regLeftRight = re.compile(r"Move one slot to the (left|right).")
    regContinue = re.compile(r"Continue with state ([A-Z])")

    start = regStart.findall(lines)[0]
    steps = int(regSteps.findall(lines)[0])
    stateLetters = regState.findall(lines)
    currValues = regValue.findall(lines)
    writtenValues = regWrite.findall(lines)
    directions = regLeftRight.findall(lines)
    nextStep = regContinue.findall(lines)

    for letter in stateLetters:
        index = stateLetters.index(letter)
        info = currValues[2*index:2*index+2] + writtenValues[2*index:2*index+2] + \
               directions[2*index:2*index+2] + nextStep[2*index:2*index+2]
        states.setdefault(letter, info)

    return start, steps, states

#MAIN
with open("data.txt","r") as file:
    lines = file.read()

cursor = 0
tape = {0:"0"} #index: value

currentState, steps, states = defineStates(lines)

#['0', '1', '1', '0', 'right', 'left', 'B', 'B']
#current value, written value, move, next
for x in range(steps):
    currentStateDescription = states[currentState]
    if tape[cursor] == currentStateDescription[0]:
        offset = 0
    elif tape[cursor] == currentStateDescription[1]:
        offset = 1
    tape[cursor] = currentStateDescription[2 + offset]
    if currentStateDescription[4 + offset] == "right":
        cursor += 1
    else:
        cursor -= 1
    currentState = currentStateDescription[6 + offset]
    tape.setdefault(cursor, "0")

result = len(list((filter(lambda x: x == "1", tape.values()))))
print(result)