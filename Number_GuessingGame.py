# # Guessing Game----------------------------------------------------------------------
secret_number = 10
guess_limit = 3
i = guess_limit

for guess_count in range(guess_limit):
    user_input = int(input("Enter your guess: "))
    guess_count += 1
    if user_input == secret_number:
        print("Congratulations! You have guessed it right")
        break
    else:
        i -= 1
        print("Wrong Guess! Only " + str(i) + " left")


