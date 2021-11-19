import random
def intro():
    print('\t _______________________________________________________________')
    print('\t|                                                               |')
    print('\t|  This is a program to play guessing a word in a words list.   |')
    print('\t|_______________________________________________________________|\n')

def get_user_list() -> list:
    user_list = []
    print('Enter words to add to the list. Enter "end" to finish. \nNote: The game is not case sensitive.')
    while True:
        user_input = input('Enter a word: ')
        if user_input != 'end':
            user_list.append(user_input)
        else:
            break
    print('='*60)
    return user_list


def check_guess(user_guess : str, list_of_words: list) -> bool:
    if user_guess.lower() in list_of_words:
        return True
    else:
        return False

def guess_word(list_of_words : list) -> str:
    while True:
        user_guess = input('Enter your guess: ')
        if user_guess.isalpha():
            if check_guess(user_guess, list_of_words):
                break
            else:
                print('Invalid guess, not in list. Try again!')
    return user_guess


def run_game():
    intro()
    list_of_words = get_user_list()
    print('words list:', list_of_words)
    number = ''
    while not isinstance(number, int):
        try:
            number = int(input('Enter desired anumber of tries: '))
        except ValueError:
            print('You didn\'t enter a number! Enter a number please.')
    
    answer = random.choice(list_of_words)
    for i in range(number):
        print('-'*60)
        print('Number of tries left:', number-i)
        user_guess = guess_word(list_of_words)
        if user_guess.lower() == answer:
            print('You won!')
            print('='*60)
            return
        else:
            print('Wrong guess.')
    print(f'Sorry. You lost! The answer was: {answer}.')
    print('='*60)

run_game()