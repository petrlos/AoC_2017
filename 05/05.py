#Advent of Code 2017 Day 05:

def task1(numbers):
    location = 0
    counter = 0
    while location < len(numbers):
        newLocation = location + numbers[location]
        numbers[location] += 1
        location = newLocation
        counter += 1
    return counter

def task2(numbers):
    location = 0
    counter = 0
    while location < len(numbers):
        newLocation = location + numbers[location]
        if numbers[location] >= 3:
            numbers[location] -= 1
        else:
            numbers[location] += 1
        location = newLocation
        counter += 1
    return counter

with open("data.txt", "r") as file:
    numbers = [int(x) for x in file.read().splitlines()]
print("Task1:",task1(numbers))

with open("data.txt", "r") as file:
    numbers = [int(x) for x in file.read().splitlines()]
print("Task2:",task2(numbers))