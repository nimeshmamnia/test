my_list = [1, 4, 7, 2, 5, 9, 3]
your_number = int(input("Enter your number"))
print("My list is" + str(my_list))
j = 0
for i in my_list:
    if i == your_number:
        j = 1

if bool(j):
    print("Your number is present in my list and is " + str(your_number))
else:
    print("Sorry! Number not found")