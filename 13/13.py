#Advent of Code 2017 - Day 13
import re
from datetime import datetime
start = datetime.now()

def getCurrentLocation(time, offset):
    if time - offset in layers.keys():
        #spocita lokakci skeneru na urcite hladine v urcitem casu, odpovida indexu v poli dict layers
        depths = layers[time-offset]
        #kontrola preteceni
        currentLocationIndex = time % len(layers[time-offset])
        currentLocation =  depths[currentLocationIndex]
        #pokud je rovna nula - paket byl chycen
        if currentLocation == 0:
            return (max(depths)+1) * time
    return 0

#MAIN
regexNum = re.compile(r"\d+")

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

#vytvori dict ve formatu range: depth, pricemz depth obsahuje sekvenci 0, 1, .. max depth, .. 2, 1
layers = {}
for line in lines:
    numbers = [int(x) for x in regexNum.findall(line)]
    layerRange = list(range(0, numbers[1], 1)) + list(range(numbers[1]-2, 0, -1))
    layers.setdefault(numbers[0], layerRange)

result = 0

#Task 1: packet se posle v case 0 - offset je nastaven na 0
for time in range(max(layers.keys())+1):
    result += getCurrentLocation(time, 0)
print("Task 1:",result)

#Task 2: hleda se offset takovy, aby vysledek byl 0
offset = 0
while True:
    result = 0
    for time in range(offset, max(layers.keys()) + 1 + offset):
        result += getCurrentLocation(time, offset)
        #pokud bude result > 0, tzn. bude chycen, neni potreba propocitavat zbytek pole
        if result > 0:
            break
    #pokud je result == 0, mame spravny offset bez zachytu
    if result == 0:
        break
    offset += 1
    if offset % 250000 == 0:
        print("Totally checked:",offset)
print("Task 2:", offset)
print("Total runtime:", datetime.now() - start)