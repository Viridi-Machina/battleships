from computer import *
from run import *

ships_player = {
    'cruiser': [2.0],
    'submarine': [3.0],
    'destroyer': [3.1],
    'battleship': [4.0],
    'aircraft_carrier': [5.0]
}

def player_creation():
    try:
        manual_placement = input('Would you like to place your own ships? Y / N\n')
        choice = manual_placement.upper().strip()

        if choice == 'Y':
            print('\n')
            
            
            
            
            
            # while confirm == 'N':
            #     cpu_creation(**ships_player)
            #     for value in ships_player.values():
            #         ship_sunk.extend(value)
            #     display_grid(hits, misses, ship_sunk)
            #     choice_2 = input('Confirm layout? Y / N\n')
            #     confirm = choice_2.upper().strip()

                            



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


player_creation()