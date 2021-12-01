#Advent of Code 2017: Day 22
from gridprint import gridPrint

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def initializeGrid(lines, startLocation):
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                grid.setdefault((x, y), "I")
    grid.setdefault(startLocation, "C")
    return grid

def weakerVirus(grid, location, direction):
    counter = 0
    for _ in range(10000):
        if grid[location] == "I":  # is infected:
            direction = (direction + 1) % 4
            grid[location] = "C"
        else:  # not infected
            direction = (direction + 3) % 4
            grid[location] = "I"
            counter += 1
        location = tupleSum(location, directions[direction])
        # pokud nova lokace neni v grid, prida ji jako False - nenakazenou
        grid.setdefault(location, "C")
    return counter

def strongerVirus(grid, location, direction):
    counter = 0
    for burst in range(10000000):
        if grid[location] == "C":
            direction = (direction + 3) % 4 #turns left
            grid[location] = "W"
        elif grid[location] == "W":
            #dont change direction
            counter += 1
            grid[location] = "I"
        elif grid[location] == "I":
            direction = (direction + 1) % 4 #turn right
            grid[location] = "F"
        elif grid[location] == "F":
            grid[location] = "C"
            direction = (direction + 2) % 4
        location = tupleSum(location, directions[direction])
        # pokud nova lokace neni v grid, prida ji jako False - nenakazenou
        grid.setdefault(location, "C")
    return counter

#MAIN
with open("data.txt", "r") as file:
    lines = file.read().splitlines()

#turn right - increase index, turn left lower index - URDL
directions = [(0,-1), (1,0), (0,1), (-1,0)]
start = (12,12)

#Task1:
grid = initializeGrid(lines, start)
task1 = weakerVirus(grid, start, 0)
print("Task 1:", task1)

#Task2:
grid = initializeGrid(lines, start)
task2 = strongerVirus(grid, start, 0)
print("Task 2:", task2)