#Advent of Code 2017 - Day 4:
def task1(line):
    for index1, word1 in enumerate(line.split(" ")):
        for index2 ,word2 in enumerate(line.split(" ")):
            if word1 == word2 and index1 != index2:
                return False
    return True

def task2(line):
    for index1, word1 in enumerate(line.split(" ")):
        for index2 ,word2 in enumerate(line.split(" ")):
            if "".join(sorted(word1)) == "".join(sorted(word2)) and index1 != index2:
                return False
    return True

#MAIN
with open("data.txt", "r") as file:
    lines = file.read().splitlines()

counter = 0
for line in lines:
    if task1(line):
        counter += 1
print("Task1:",counter)

counter = 0
for line in lines:
    if task2(line):
        counter += 1
print("Task2:",counter)