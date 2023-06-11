from collections import defaultdict

def get_value(v):
    try:
        return int(v)
    except ValueError:
        return registers[v]

def perform_instruction(instruction, current_line, mul_counter):
    instruction = instruction.split(" ")
    if instruction[0] == "set":
        registers[instruction[1]] = get_value(instruction[2])
    elif instruction[0] == "sub":
        registers[instruction[1]] -= get_value(instruction[2])
    elif instruction[0] == "mul":
        registers[instruction[1]] *= get_value(instruction[2])
        mul_counter += 1
    elif instruction[0] == "jnz":  # "JNZ X Y" - triggers only, if X != 0
        if get_value(instruction[1]) != 0:
            current_line += int(instruction[2]) - 1
    current_line += 1
    return current_line, mul_counter

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

registers = defaultdict(int)
registers["a"] = 0

current_line = 0
mul_counter = 0
while current_line < len(lines):
    current_line, mul_counter = perform_instruction(lines[current_line], current_line, mul_counter)
    print(mul_counter, registers)

print(mul_counter)