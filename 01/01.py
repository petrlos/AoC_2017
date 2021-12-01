#Advent of Code 2017: Day 01

def task1(input):
    input = input + input[0]

    sum = 0
    for index in range(0,len(input)-1):
        if input[index] == input[index+1]:
           sum += int(input[index])
    return sum

def task2(input):
    sum = 0
    for index in range(0,len(input)):
        newIndex = int(index + len(input) / 2)
        if newIndex > len(input)-1:
            newIndex = newIndex - len(input)
        if input[index] == input[newIndex]:
            sum += int(input[index])
    return sum

with open("data.txt", "r") as file:
    captcha = file.read()


print("Task 1:", task1(captcha))
print("Task 2:", task2(captcha))
