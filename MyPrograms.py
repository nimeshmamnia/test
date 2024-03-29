# Write a Python program to find a list of integers with exactly two occurrences
# of one and at least three occurrences of five. Return True otherwise False

'''my_list = list(input("Enter List Elements: "))
count1 = 0
count5 = 0
for items in my_list:
    if items == str(1):
        count1 = count1 + 1
    elif items == str(5):
        count5 = count5 + 1
if count5 >= 3 and count1 == 2:
    print(True)
else:
    print(False)
'''
#------------------------------------------------------------------------------------------------------------------------------------

# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile
# but as few as possible.
# Write a Python program to find the number of stones in each pile.

'''stones = int(input("Enter a number: "))
i = 0
pile = stones
while i < stones:
    print(pile)
    i += 1
    pile += 2'''
#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

'''num = int(input("Enter your number (1500 - 2700): "))
if num % 5 == 0 and num % 7 == 0:
    print("Wow! Your number", num, "is divisible by 7 and is multiples of 5")
else:
    print("Sorry!", num, "is not divisible by 7 and is not multiples of 5 either")'''

#------------------------------------------------------------------------------------------------------------------------------------
#Write a Python program to convert temperatures to and from Celsius and Fahrenheit

'''temperature = float(input("Enter the temperature either in Celsius or Fahrenheit: "))
units = input("What's the unit of your inputted number? F - Fahrenheit or C - Celsius ")

if units == 'F':
    celsius = 5 * (temperature - 32) / 9
    print(" Your temperature in Fahrenheit is", temperature, "and in Celsius is", celsius)

if units == 'C':
    fahrenheit = 9 * temperature / 5 + 32
    print(" Your temperature in Fahrenheit is", fahrenheit, "and in Celsius is", temperature)
'''
#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

'''guessed_num = 7
count = 3
correct_guess = 0

while count != 0:
    user_num = int(input("Enter your number between 1 and 9"))
    if guessed_num != user_num:
        print("Wrong Guess!")
        count = count - 1
    else:
        count = 0
        correct_guess = 1

if correct_guess == 1:
    print("Correct Guess!")
else:
    print("You guessed wrong all the times")'''
#------------------------------------------------------------------------------------------------------------------------------------
#  Write a Python program to construct the following pattern, using a nested for loop.
'''count = 1
while count < 5:
    print("*" * count)
    count = count + 1

while count >= 1:
    print("*" * count)
    count = count - 1'''

#------------------------------------------------------------------------------------------------------------------------------------
# 5. Write a Python program that accepts a word from the user and reverses it.
# Prompt the user to input a word
'''word = input("Input a word to reverse: ")
print(word[::-1])'''

#------------------------------------------------------------------------------------------------------------------------------------
#  Write a Python program to count the number of characters (character frequency) in a string.
'''word = input("Enter your string: ")
my_dict = dict()
for keys in word:
    my_dict[keys] = my_dict.get(keys, 0) + 1

print(my_dict)'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.

'''my_string = input("Enter your string: ")
new_string = ''
length = len(my_string)
if length < 2:
    print("your string is too short")
else:
    new_string = my_string[0:2] + my_string[length-2:]

print(new_string)'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to get a string from a given string where
# all occurrences of its first char have been changed to '$', except the first char itself.

'''my_string = input("Enter your string:")
first_char = my_string[0]
for char in my_string:
    if char == first_char:
        my_string = my_string.replace(char, '$')

print(first_char + my_string[1:])'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#if len(my_string) > 3 and my_string

'''my_string = input("Enter your string:")
len = len(my_string)

if len > 3 and my_string.endswith('ing'):
    new_string = my_string[:len-3] + 'ly'
elif len > 3 and my_string[len-3:] != 'ing':
    new_string = my_string + 'ing'
else:
    new_string = my_string

print(new_string)'''
#------------------------------------------------------------------------------------------------------------------------------------
#7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

'''my_string = input("Enter your string which contains not and poor: ")
length = len(my_string)
snot = my_string.find('not')
spoor = my_string.find('poor')
new_string = my_string
if spoor > snot and snot > 0 and spoor > 0:
    new_string = my_string[:snot] + 'good'
print(new_string)'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
'''my_string = input("Enter your string: ")
print("your string in lower cases is: ", my_string.lower())
print("your string in upper cases is: ", my_string.upper())'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python function to reverse a string if its length is a multiple of 4.
'''my_string = input("Enter your string: ")
new_string = my_string
length = len(my_string)
if length % 4 == 0:
    # new_string = ''.join(reversed(my_string))
    new_string = my_string[::-1]
    

print(new_string)'''

#------------------------------------------------------------------------------------------------------------------------------------
#lists
#1. Write a Python program to sum all the items in a list.
'''def sumoflist(lst):
    addition = 0
    for items in lst:
        addition = addition + items
    return addition


my_list = [1,2,3,4,5,6,7,8,9]
print("Sum of all elements in list is: ", sumoflist(my_list))'''

#------------------------------------------------------------------------------------------------------------------------------------
# 2. Write a Python program to multiply all the items in a list.
'''def muloflist(lst):
    multiplication = 1
    for items in lst:
        multiplication = multiplication * items
    return multiplication


my_list = [1,2,3,4,5,6,7,8,9]
print("Multiplication of all elements in list is: ", muloflist(my_list))'''

#------------------------------------------------------------------------------------------------------------------------------------
# 3. Write a Python program to get the largest number from a list.

'''my_list = [1,2,10,4,5,45,7,8,9]
my_list.sort()
print("Largest number is: ", my_list[len(my_list)-1])'''

#------------------------------------------------------------------------------------------------------------------------------------
# 4. Write a Python program to get the smallest number from a list.

'''my_list = [1,2,10,4,5,45,7,8,9]
my_list.sort()
print("Largest number is: ", my_list[0])'''

#------------------------------------------------------------------------------------------------------------------------------------
# 7. Write a Python program to remove duplicates from a list. and if the list is empty or not

'''my_list = list(input("Enter List elements: "))
new_list = list()

if len(my_list) > 0:
    for items in my_list:
        if items not in new_list:
            new_list.append(items)
    print(new_list)
else:
    print("List is Empty")'''

#------------------------------------------------------------------------------------------------------------------------------------
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

'''def compare_list(list1, list2):
    match = 0
    for items1 in list1:
        for items2 in list2:
            if items1 == items2:
                match = 1
    if match == 1:
        print("There are some common elements in both the lists")
    else:
        print("Both lists are unique")

list1 = list(input("Enter elements of List 1: "))
list2 = list(input("Enter elements of List 2: "))

compare_list(list1, list2)'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

'''sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color = [sample_list[i] for i in range(len(sample_list)) if i not in [0, 4, 5]]

print(color)'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order

'''my_str = input("Enter a string: ")
my_list = my_str.split()
my_list_reversed = my_list[::-1]
print(' '.join(my_list_reversed))'''

#------------------------------------------------------------------------------------------------------------------------------------
# Write a program (using functions!) that check if the string user has input is palindrome or not
'''def isPalindrome(s):
    return s == s[::-1]

my_string = input("Enter your string: ")
if isPalindrome(my_string):
    print("Is Palindrome")
else:
    print("Is Not Palindrome")'''

# --------------------- Group all anagram words together -----------------------------
'''strs = ["eat","tea","tan","ate","nat","bat"]
anagram_groups = {}
for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = [word]
            else:
                anagram_groups[sorted_word].append(word)

print(anagram_groups.values())'''

#------------------------------ Calculate x power n ----------------------------------
'''x = int(input(" Enter base number: "))
n = int(input(" Enter power number: "))

if n == 0:
    print (1)
else:
    temp = 1
    base, power = x, abs(n)
    while power >= 1:
        if power % 2 == 0:
            base = base * base
            power = power // 2
        else:
            temp = temp * base
            power -= 1
    print(temp) if n > 0 else print(1/temp)'''

# -------------------------------------------- Sqrt of x (using Binary search)-----------------------------------------------
'''x = int(input(" Enter x: "))
a = 0
b = x
while abs(a - b) != 1:
    mid = (a + b) // 2
    print("mid in while loop = ", mid)
    if mid * mid == x:
        print("if mid*mid == x", mid*mid)

    if mid * mid > x:
        print("mid * mid > x ", mid * mid)
        b = mid
        print("b = ", b)
    else:
        a = mid
        print("a = ", a, "mid = ", mid)

print(a)'''

#-------------------------------- Merge Intervals------------------------
'''
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
list1 = [intervals[0]]
for start, end in intervals[1:]:
    if start <= list1[-1][1]:
        list1[-1][1] = max(end,list1[-1][1])
    else:
        list1.append([start, end])
print(list1)
'''
#-------------------------------Insert intervals -----------------------------------
'''intervals = [[1,3],[6,9]]
newInterval = [2,5]
i=0
n = len(intervals)
res=[]
while i < n and intervals[i][1] < newInterval[0]:
    res.append(intervals[i])
    i += 1
while i < n and intervals[i][0] <= newInterval[1]:
    newInterval[0] = min(intervals[i][0], newInterval[0])
    newInterval[1] = max(intervals[i][1], newInterval[1])
    i += 1
res.append(newInterval)
while i < n:
    res.append(intervals[i])
    i += 1
print(res)'''
#----------------------------------
#------------------------------------------------------------------------------------------------------------------------------------




