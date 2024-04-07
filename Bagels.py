import random

NUM_DIGITS = 3
MAX_GUESS = 10


def getclues(number, secret_number):
    clues = []
    for i in range(len(number)):
        if number[i] == secret_number[i]:
            clues.append('Fermi')
        elif number[i] in secret_number:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        return ' '.join(clues)


def getsecretnumber():
    numbers = list('1234567890')
    random.shuffle(numbers)
    sec_number = ''
    for i in range(NUM_DIGITS):
        sec_number += str(numbers[i])
    return sec_number


'''Following approach can work too, but in that case there is a possibility of same digits forming 3 digit number'''
# def getsecretnumber():
#     count = 0
#     sec_number = 0
#     while count != NUM_DIGITS:
#         num = random.randrange(9)
#         sec_number = sec_number * 10 + num
#         count +=1
#     return str(sec_number)

secret_number = getsecretnumber()

print('''Bagels, a deductive logic game.
I am thinking of a ''', NUM_DIGITS, '''- digit number with no repeated digits. Try to guess what it is. 
Here are some clues: 
When I say --> That means:
1. Pico - One digit is correct but in the wrong position.
2. Fermi - One digit is correct and in the right position.
3. Bagels - No digit is correct.
I have already guessed a number and you have''', MAX_GUESS, '''guesses left''')
print(secret_number)
numGuesses = 1
while numGuesses < MAX_GUESS:
    number = input('Enter 3 digit number: ')
    if number == secret_number:
        print('You got it')
        break
    else:
        clues = getclues(number, secret_number)
        print(clues)
        print('You have', MAX_GUESS - numGuesses, 'guesses left')
        numGuesses += 1

if numGuesses > MAX_GUESS:
    print('Sorry! you ran out of guesses')
    print('Correct answer was', secret_number)
    print('Thanks for playing')
