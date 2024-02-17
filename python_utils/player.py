#from python_utils.stats import *


def player_creation(ships_player):
    
    choices = ['Y', 'N']
    try:
        manual_placement = input('Would you like to place your own ships? Y / N\n')
        choice = manual_placement.upper().strip()

        if choice == 'Y':
            print('\n')
       
        if choice == 'N':
            pass

            # if str.isalpha(guess[0]) == False:
            #     print('First co-ordinate must be a letter A-J.')
            # elif guess[0].upper() not in grid_letters:
            #     print('The first co-ordinate must be a letter A-J.')
            # elif guess[1:] not in grid_numbers:
            #     print('Second co-ordinate must be a number 1-10.')
            # elif guess in guesses:
            #     print('Grid location already fired upon, please select a new target.')
            # else:
            #     valid = 1
            #     break
    except:
        print('Incorrect input, please try a new co-ordinate.\nFor example "D7"')
    
    return choice

