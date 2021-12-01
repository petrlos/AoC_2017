#Advent of Code Day 19 - 2017
#provede soucet odpovidajicich clenu ve dvou tuple
def tupleSum(a,b):
    return tuple(map(sum, zip(a, b)))

def getNewDirection(currentDirection, pointCoords):
#pokud je aktualni smer nahoru/dolu, podiva se doprava/doleva jestli tam existuje bod a podle toho nastavi novy smer
#resp aktualne vpravo/vlevo nastavi novy smer nahoru/dolu
    if currentDirection == 0 or currentDirection == 1:
        if tupleSum(pointCoords, dirDULR[2]) in grid.keys():
            newDirection = 2
        if tupleSum(pointCoords, dirDULR[3]) in grid.keys():
            newDirection = 3
    elif currentDirection == 2 or currentDirection == 3:
        if tupleSum(pointCoords, dirDULR[0]) in grid.keys():
            newDirection = 0
        if tupleSum(pointCoords, dirDULR[1]) in grid.keys():
            newDirection = 1
    return newDirection

#MAIN

fileName = "data.txt"; coords = (0,135)
with open(fileName, "r") as file:
    lines = file.read().splitlines()

#grid dict ve formatu souradnice: bod, pokud je bod mezera, nenacte ho vubec
grid = {}
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char != " ":
            grid.setdefault((x,y), char)

result = ""
counter = 0; currentDirection = 0
dirDULR = [(+1, 0), (-1, 0), ( 0,-1), (0, 1)]

#prochazi grid aktualnim smerem, pokud narazi na "+", zmeni smer, pokud na pismeno, ulozi ho do result
#while cyklus konci v okamziku, kdy narazi na souradnice, ktere uz nejsou v grid.keys()
while True:
    counter += 1
    newCoords = tupleSum(coords, dirDULR[currentDirection])
    if newCoords not in grid.keys():
        break
    if grid[newCoords] == "+":
        currentDirection = getNewDirection(currentDirection, newCoords)
    elif grid[newCoords].isalpha():
        result += grid[newCoords]
    coords = newCoords

print("Task 1:", result)
print("Task 2:", counter)
