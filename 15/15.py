#Advent of Code 2017 - Day 15
def getNewNumber(number, multiplicator):
    return (number * multiplicator) % 2147483647

def judge(valueA, valueB):
    return bin(valueA)[-16:] == bin(valueB)[-16:]

def task1(genAValue, genBValue):
    print("Task 1 started")
    counter = 0
    for i in range(0, 40000000):
        genAValue = getNewNumber(genAValue, multiplicatorA)
        genBValue = getNewNumber(genBValue, multiplicatorB)
        if judge(genAValue, genBValue):
            counter += 1
        if i % 2000000 == 0:
            print("{0} % done.".format(i / 40000000 * 100))
    return counter

def task2(genAValue, genBValue):
    print("Task 2 started")
    counter = 0
    for i in range(0,5000000):
        while True:
            genAValue = getNewNumber(genAValue, multiplicatorA)
            if genAValue % 4 == 0:
                break
        while True:
            genBValue = getNewNumber(genBValue, multiplicatorB)
            if genBValue % 8 == 0:
                break
        if judge(genAValue, genBValue):
            counter += 1
        if i % 500000 == 0:
            print("{0} % done.".format(i / 5000000 * 100))
    return counter

#MAIN

multiplicatorA = 16807; multiplicatorB = 48271
genAValue = 703; genBValue = 516

#print("Task 1:", task1(genAValue, genBValue))
print("Task 2:", task2(genAValue, genBValue))