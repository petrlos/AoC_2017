#Advent of Code 2017: Day 23
def coprocessor(a): #instructions rewritten in code
    h, counter = 0, 0
    if a == 0:
        b = c = 57
    else:
        b = 105700
        c = 122700

    while True:
        f = True
        d = 2
        while True:
            e = 2
            while True:
                counter += 1
                if e * d  == b: #works with none primes only
                    f = False
                e += 1
                if e == b:
                    break
            d += 1
            if d == b:
                break
        if not f : #if f == false - h+1
            h += 1
        if b != c:
            b += 17
        else:
            break
    return counter

def remove_numbers_divisible_by(divisor, numbers):
    for number in list(numbers):
        if number != divisor and number % divisor == 0:
            numbers.remove(number)
    return numbers

#Coprocessor starts without modifications
print("Task 1:",coprocessor(0))

#no need to start coprocessor: result are NONE-prime numbers in range 105700-122700 in step of 17
n = 123000 #get all primes in this range
numbers = set(range(2,n))
for number in range(2, int(n ** 0.5) + 1):
    numbers = remove_numbers_divisible_by(number, numbers)

#all possible "b" numbers
bees = set(range(105700, 122700+1, 17))
result = len(bees - numbers)
print("Task 2:",result) #difference of sets - alls bees, that are NONE-prime