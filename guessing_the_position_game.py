lst = ['', '', 'O']

# FUNCTION TO RANDOMIZE THE LIST


def randomize_list(lst1):
    from random import shuffle
    shuffle(lst1)
    return lst1

# FUNCTION TO TAKE INPUT FROM THE USER


def user_input():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Please enter your guessed index: 0 , 1 , 2:')
    return int(guess)

# function to check if the guessed index contains 'O'


def check_guess(lst2, guess):
    if lst2[guess] == 'O':
        print('Congrats your guess were right')
    else:
        print('better luck next time')
        print(lst2)


# FUNCTION CALLING

random_list = randomize_list(lst)

guessed_index = user_input()

check_guess(random_list, guessed_index)
