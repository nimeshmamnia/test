num = int(input("Enter the last number of Fibonacci series"))
total = 0
a = 0
b = 1
if num == a:
    print("Fibonacci Series is ", a)
elif num == b:
    print("Fibonacci Series is " + str(b))
else:
    print("Fibonacci Series is: ")
    for i in range(num+1):
        print(total)
        total = a + b
        a = b
        b = total


