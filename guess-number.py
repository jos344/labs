import sys

MAGIC = 34
number_of_guess = 0

def show_menu():
    print('============================================')
    print('         WELCOME TO MAGIC NUMBER GAME       ')
    print('============================================')

def guess():
    guess = int(input('Your guess: '))
    global number_of_guess
    number_of_guess += 1
    if guess > MAGIC: 
        print('Too high')
    elif guess < MAGIC:
        print('Too low')
    elif guess == MAGIC:
        print('You guessed correct!')
        play_again()

def play_again():
    play = input('Do you want to play again? Y/N ')
    if play == 'Y':
        guess()
    if play == 'N':
        sys.exit() 

show_menu()
print('Guess the magic number\nYou have 5 chances')
while True:
    guess()
    if number_of_guess >= 5:
        sys.exit()