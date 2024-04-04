import random, sys
user_win = 0
computer_win = 0
tie = 0
while True:
    game = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(game)
    user_choice = input("Enter your choice: (rock, paper, scissor) or QUIT- ")
    print("\nYour choice is: " + user_choice + " and computers choice is: " + computer_choice)
    if user_choice.upper() == 'QUIT':
        print("Thanks for playing")
        sys.exit()
    elif user_choice == computer_choice:
        print("It's a tie")
        tie += 1
    elif user_choice == 'rock' and computer_choice == 'scissor':
        print("You win")
        user_win += 1
    elif user_choice == 'scissor' and computer_choice == 'paper':
        print("You win")
        user_win += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win")
        user_win += 1
    else:
        print("You loose")
        computer_win += 1
    print('Score: You = ', user_win, "Computer = ",computer_win, "Tie = ", tie)