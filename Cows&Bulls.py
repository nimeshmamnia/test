import random, sys

computer_choice = random.randint(1, 5000)
while True:
    cows = 0
    bulls = 0
    user_choice = input("Enter a number (1-5000) or QUIT: ")
    user = int(user_choice)
    if 0 > user > 5000:
        print("Please enter valid range")
        continue
    elif user_choice.upper() == 'QUIT':
        print("Thanks for playing\nScore is: Cows = ", cows, "Bulls = ", bulls)
    str_cc = str(computer_choice)
    for i in range(len(user_choice)):
        if user_choice[i] in str_cc:
            cows += 1
        else:
            bulls += 1
