#Advent of Code 2017 - Day 11
def countDistance(actual):
    #parametry ma typ tuple
    x1, y1 = 0, 0
    x2, y2 = actual[0], actual[1]
    #formulka ze stackoverflow na vypocet "manhattan" vzdalenosti v hexgrid
    return max( [abs(x1 - x2), abs(y1 -y2), abs( (-x1 + -y1) - (-x2 + -y2) )])

with open("data.txt", "r") as file:
    data = file.read().split(",")

hexGridWays = {"n":(0,1), "s":(0,-1), "nw":(-1,1), "sw":(-1,0), "ne":(1,0), "se":(1,-1)}
position = (0,0)
distances = []

for coord in data:
    direction = hexGridWays[coord]
    position = tuple(map(lambda x, y: x + y, position, direction))
    distances.append(countDistance(position))

print("End position",position)
print("Task 1:", countDistance(position))
print("Task 2:", max(distances))