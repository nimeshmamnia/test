import math, sys

while True:
    res = input("Enter a a positive whole number to factor (or QUIT):  ")
    if res.upper() == 'QUIT':
        sys.exit()
    if not res.isdecimal() or int(res) < 0:
        continue
    number = int(res)

    factorial = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factorial.append(i)
            factorial.append(number // i)
    factorial.sort()
    if len(factorial) == 2:
        print(number, 'is a prime number')
    else:
        print(number, 'is a composite number')
