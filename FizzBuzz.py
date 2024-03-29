# FizzBuzz Game.. The FizzBuzz game is a classic programming exercise. The goal is to print the numbers from 1 to 100, but instead of multiples of 3, print "Fizz", and instead of multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)
