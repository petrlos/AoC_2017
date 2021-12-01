#Advent of Code 2017 - Day 21

#TODO: Fractal Art - prekladani obrazku, nahrazovani retezce, otaceni matice znaku

with open("test.txt") as file:
    lines = file.read().splitlines()

grid = ".#./..#/###".split("/")
print(grid)


rules = {}

for line in lines:
    newRule = line.split(" => ")