#Advent of COde 2017: Day 20
from Particle import Particle
import re, datetime
start = datetime.datetime.now()

def generateParticles(lines):
    particles = []
    partDistance = {}
    for partNr, line in enumerate(lines):
        numbers = [int(x) for x in regNum.findall(line)]
        newParticle = Particle(partNr, numbers)
        partDistance.setdefault(partNr, newParticle.distance)
        particles.append(newParticle)
    return particles, partDistance

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

regNum = re.compile(r"-?\d+")

#Task 1: 500 iteraci je dostatecny, aby byla nalezena castice nejblizsi souradnicim 0,0,0
result = 0
particles, partDistance = generateParticles(lines)
for _ in range(500):
    for particle in particles:
        particle.stepByOne()
        partDistance[particle.partNr] = particle.distance
    minDist = min(partDistance.values())
    for key in partDistance.keys():
        if partDistance[key] == minDist:
            result = key
print("Task 1:", result)

#Task 2: 40 iteraci je dostatecnych, aby se vyloucily vsechny interakce
particles, partDistance = generateParticles(lines)
for i in range(40):
    for particle in particles:
        particle.stepByOne()
    for x, part1 in enumerate(particles):
        for y, part2 in enumerate(particles):
            if x != y:
                if part1.location == part2.location:
                    part1.active = False
                    part2.active = False
counter = 0
for particle in particles:
    if particle.active:
        counter += 1
print("Task 2:",counter)
print("Runtime: ", datetime.datetime.now() - start)