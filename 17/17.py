#Advent of Code 2017 Day 17
from datetime import datetime
start = datetime.now()

circullarBuffer = [0]; currentPosition = 0; step = 354; result = 0

for number in range(1, 2018):
    insertLocation = (currentPosition + step) % len(circullarBuffer)
    circullarBuffer.insert(insertLocation+1, number)
    currentPosition = circullarBuffer.index(number)
index2017 = circullarBuffer.index(2017)

print("Task 1:",circullarBuffer[index2017+1])

currentPosition = 0
for number in range(1, 50000001):
    insertLocation = (currentPosition + step) % number
    if insertLocation == 0:
        print("Numbers put right from zero:",number)
        result = number
    currentPosition = insertLocation + 1
    if number % 5000000 == 0:
        print("Done: ",number * 100/50000000)

print("Task 2 final result:",result)
print("Total runtime: ", datetime.now() - start)