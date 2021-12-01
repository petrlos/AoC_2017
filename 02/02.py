#Advent of Code 2017 Day 2
def task1(lines):
    checksum = []
    for line in lines:
        numbers = [int(x) for x in line.split(" ")]
        checksum.append(max(numbers) - min(numbers))
    return sum(checksum)

def divisorGenerator(number):
    divisors = []
    for i in range(2, int(number/2+1)):
        if number % i == 0:
            divisors.append(i)
    return divisors

def task2(lines):
    checksum = []
    for line in lines:
        numbers = [int(x) for x in line.split(" ")]
        for number in numbers:
            divisors = divisorGenerator(number)
            for divisor in divisors:
                if divisor in numbers:
                    checksum.append(int(number / divisor))
    return sum(checksum)

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

lines = [" ".join(line.split()) for line in lines]

checksum = []
for line in lines:
    numbers = [int(x) for x in line.split(" ")]
    checksum.append(max(numbers) - min(numbers))

print("Task 1:", task1(lines))
print("Task 2:", task2(lines))