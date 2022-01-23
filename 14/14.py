#Advent of Code 2017: Day 14:
from knotHashFunc import knotHash
from collections import deque

def generateGrid(keyString):
    grid = {}
    for row in range(128):
        key = keyString + "-{0}".format(row)
        rowHashed = knotHash(key)
        gridRow = ""
        for char in rowHashed:
            gridRow += bin(int(char, 16))[2:].rjust(4, "0")
        for column, char in enumerate(gridRow):
            if char == "1":
                grid[row, column] = "1"
    return grid

def deleteRegion(coords):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UDLR
    queue = deque([coords])
    grid[queue[0]] = "0"
    while queue:
        for _ in range(len(queue)):
            currentPoint = queue[0]
            for direction in directions:
                possibleNeighbour = tuple([x + y for x, y in zip(direction, currentPoint)])
                if possibleNeighbour in grid.keys():
                    if grid[possibleNeighbour] == "1":
                        queue.append(possibleNeighbour)
                        grid[possibleNeighbour] = "0"
            queue.popleft()

def countRegions(grid):
    regions = 0
    for row in range(128):
        for column in range(128):
            if (row, column) in grid.keys():
                if grid[row, column] == "1":
                    regions += 1
                    deleteRegion((row, column))
    return regions

#MAIN
keyString = "xlqgujun"

grid = generateGrid(keyString)
print("Task 1:", len(grid.values()))
print("Task 2:", countRegions(grid))