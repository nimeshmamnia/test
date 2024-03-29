# Rock-Paper-Scissors Game:

import random

game = ['rock', 'paper', 'scissor']
computer_choice = random.choice(game)

user_input = input("Enter your choice (rock, paper, scissor): ")
print("\nYour choice is: " + user_input + " and computers choice is: " + computer_choice)

if user_input == computer_choice:
    print("\nIt's a tie")
elif user_input == 'rock' and computer_choice == 'scissor':
    print('\nYou win')
elif user_input == 'scissor' and computer_choice == 'paper':
    print('\nYou win')
elif user_input == 'paper' and computer_choice == 'rock':
    print('\nYou win')
else:
    print("You loose, computer wins")