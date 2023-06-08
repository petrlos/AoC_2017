#Advent of Code 2017: Day 18
from collections import defaultdict, deque

class Reciever_programm():

    def __init__(self, programm_id):
        self.sound = 0
        self.id = programm_id
        self.counter = 0
        self.currentline = 0
        self.queue = deque()
        self.deadlock = False
        self.registers = defaultdict(int)
        self.recover = 0

    def __str__(self):
        return "ID:{0}: {1}, {2}".format(self.id, self.registers, self.sound)

def perform_instruction(lines, current_reciever):

    def val(v):
        try:
            return int(v)
        except ValueError:
            return recievers[current_reciever].registers[v]

    inst = lines[recievers[current_reciever].currentline]
    inst = inst.split(" ")

    if inst[0] == "snd":
        recievers[current_reciever].sound = val(inst[1])
    elif inst[0] == "set":
        recievers[current_reciever].registers[inst[1]] = val(inst[2])
    elif inst[0] == "add":
        recievers[current_reciever].registers[inst[1]] += val(inst[2])
    elif inst[0] == "mul":
        recievers[current_reciever].registers[inst[1]] *= val(inst[2])
    elif inst[0] == "mod":
        recievers[current_reciever].registers[inst[1]] %= val(inst[2])
    elif inst[0] == "rcv":
        recievers[current_reciever].recover = recievers[current_reciever].sound
    elif inst[0] == "jgz":
        if recievers[current_reciever].registers[inst[1]] > 0:
            recievers[current_reciever].currentline += val(inst[2]) - 1
    recievers[current_reciever].currentline += 1
    if recievers[current_reciever].recover != 0:
        recievers[current_reciever].deadlock = True

#MAIN

with open("data.txt") as file:
    lines = file.read().splitlines()

recievers = []
for i in range(2):
    recievers.append(Reciever_programm(i))

current_reciever = 0

while not recievers[0].deadlock:
    perform_instruction(lines, current_reciever)

print("Task 1:",recievers[0].sound)