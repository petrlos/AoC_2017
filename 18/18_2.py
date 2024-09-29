# Advent of Code 2017: Day 18
from collections import deque, defaultdict

class Program:
    def __init__(self,p):
        self.id = p
        self.registers = defaultdict(int, {"p":p})
        self.queue = deque()
        self.counter = 0
        self.pointer = 0
        self.deadlock = False

    def __repr__(self):
        return f"Program {self.id}: {self.registers}, {self.queue}, counter {self.counter}, Pointer{self.pointer}"

    def get_value(self, x): #if number return number else value in register
        try:
            return int(x)
        except ValueError:
            return self.registers[x]

    def execute_line(self, line):
        send = None
        line = line.split(" ")
        inst = line[0]
        val1 = line[1]
        val2 = line[2] if len(line) > 2 else None
        if inst == "snd":
            send = self.get_value(val1)
            self.counter += 1
            self.pointer += 1
        elif inst == "rcv":
            if len(self.queue) > 0:
                value = self.queue.popleft()
                self.registers[val1] = value
                self.deadlock = False
                self.pointer += 1
            else:
                self.deadlock = True
        elif inst == "set":
            self.pointer += 1
            self.registers[val1] = self.get_value(val2)
        elif inst == "add":
            self.pointer += 1
            self.registers[val1] += self.get_value(val2)
        elif inst == "mul":
            self.pointer += 1
            self.registers[val1] *= self.get_value(val2)
        elif inst == "mod":
            self.pointer += 1
            self.registers[val1] %= self.get_value(val2)
        elif inst == "jgz":
            if self.get_value(val1) > 0:
                self.pointer += self.get_value(val2)
            else:
                self.pointer += 1
        return send

def is_deadlock(programs): #all queue must be empty, both program in deadlock to stop
    for program in programs:
        if len(program.queue) > 0:
            return False
        if program.deadlock == False:
            return False
    return True

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

programs = [Program(0), Program(1)]
current = 0

while not is_deadlock(programs):
    program = programs[current]
    send = program.execute_line(lines[program.pointer])
    if send is not None:
        programs[1-current].queue.append(send)
        program.deadlock = False
    if program.deadlock: #run as long as can
        current = 1 - current

print("Part 2:", programs[1].counter)