''' Rock PAper Scissor Game '''

import random
import os
import re
os.system('cls' if os.name == 'nt' else 'clear')

def word_by_word(word):
    for i in range(len(word)):
        print(word[i], end = '')

loop=2

while(loop<10):
    print('''
    Rock Paper Scissor Game
    -----------------------
    1. Rock
    2. Paper
    3. Scissor
    ''')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    elif choice == 3:
        choice_name = 'Scissor'
    else:
        word_by_word('Invalid choice')
        break

    print('Your choice is: ' + choice_name)
    word_by_word('Computer is thinking...')
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print('Computer choice is: ' + comp_choice_name)
    print(choice_name + ' V/s ' + comp_choice_name)
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice == 3 ) or (choice == 3 and comp_choice == 1)):
        word_by_word('computer wins ')

    elif((choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2)):
        word_by_word('YOU win =>')
    else:
        word_by_word("It's a DRAW ")

    print('Do you want to play again? (Y/N)')
    ans = input()
    if ans == 'n' or ans == 'N':
        break
    else:
        loop=2
