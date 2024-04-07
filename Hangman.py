import random
def generate_word():
    words = ["python", "program","practise", "machine", "learning", "ai", "list", "resume", "dog", "cat"]
    return random.choice(words)

max_guesses = 10
wrong_guess = 0
word = generate_word()
computer_choice = word
import random
def generate_word():
    words = ["python", "program","practise", "machine", "learning", "ai", "list", "resume", "dog", "cat"]
    return random.choice(words)

max_guesses = 10
wrong_guess = 0
word = generate_word()
computer_choice = word
word = set(word)
book = set('abcdefghijklmnopqrstuvwxyz')
used_letters = set()
correct_guess = set()
print("Welcome to Hangman game, where you guess the word chosen by the computer. You have total ",max_guesses,"wrong guesses \n")
while len(word) > 0 and max_guesses > 0:
    print("User Guess: ", ''.join(used_letters))
    user_guess = input("Guess a letter: ").lower()
    if user_guess in book-used_letters:
        used_letters.add(user_guess)
        if user_guess in word:
            correct_guess.add(user_guess)
            word.remove(user_guess)
            print("Good Job!\n")
            print("Correct Letter so far: ", ''.join(correct_guess))
        else:
            # wrong_guess += 1
            max_guesses = max_guesses-1
            print("Oops! Wrong guess. You now have", max_guesses, "guesses left\n")

    elif user_guess in used_letters:
        print("You have already used this letter. Please use different one\n")
    else:
        print("Invalid character, Please enter valid character\n")
if max_guesses == 0:
    print("Good Try. Computer Guessed word was: ", computer_choice)
else:
    print("You guessed the word correctly. Correct word was", computer_choice)