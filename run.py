# Track score and save user email for login, store score and user information on external sheet
# With enough time, allow import from external sheet (with link for users) to import ship placement

from grid import *
from computer import *
from player import *


def display_grid(**player):
    '''
    This function displays the updated grid for the player and the opponent;
    showing any hits and misses on the board, as well as the player's ships.

    Two for loops create a grid that scales based on the defined grid_size 
    variable. This is repeated for the opponent's grid.
    Adapted from a python code tutorial video-series from 
    'Dr Codie' on YouTube: https://www.youtube.com/@DrCodie
    '''
    # Forms grid top
    print('\n', grid_title_both)
    print(grid_top_both)
    
    # Forms grid bodies for both the player and the opponents's grid.
    # grid_location starts at 11 as the grid numbering starts from 1,1 (A1)
    # The player grid has an added for loop to display all their ships.
    grid_location = 11 
    grid_location_2 = 11
    for y in range(grid_size):
        grid_row = ''
        for i in range(grid_size):
            grid_element = grid 
            for value in player.values():
                if grid_location in value:
                    grid_element = sunk
            if grid_location in misses:
                grid_element = miss
            elif grid_location in hits:
                grid_element = hit
            elif grid_location in ship_sunk:
                grid_element = sunk
            grid_row = grid_row + grid_element
            grid_location = grid_location + 1
        row = f'{vertical}{spacer*2}{grid_row}{spacer}{vertical}'

        grid_row_2 = ''
        for j in range(grid_size):
            grid_element_2 = grid 
            if grid_location_2 in misses_2:
                grid_element_2 = miss
            elif grid_location_2 in hits_2:
                grid_element_2 = hit
            elif grid_location_2 in ship_sunk_2:
                grid_element_2 = sunk_2
            grid_row_2 = grid_row_2 + grid_element_2
            grid_location_2 = grid_location_2 + 1
        row_2 = f'{vertical_2}{spacer*2}{grid_row_2}{spacer}{vertical_2}'

        print(grid_letters[y], row, spacer*3, grid_letters[y], row_2)

    # Forms grid bottom
    print(grid_bottom_both)
    print(grid_numbers_string, spacer*6, grid_numbers_string, '\n'*2)


def validate_guess(guesses):
    '''
    This function validates that the user's guess is between A1 and J10
    and has not already been used.
    
    After validation the inputed guess will be converted into an uppercase 
    letter and number. Then the letter's ordinal value is combined with
    the given number to form a string, which is converted into a final
    integer that can be used to determine the shot location on the grid.
    '''
    valid = 0
    while valid == 0:
        try:
            user_guess = input('Select a co-ordinate to launch a missile: \n')
            guess = user_guess.upper().strip()
            if str.isalpha(guess[0]) == False:
                print('First co-ordinate must be a letter A-J.')
            elif guess[0].upper() not in grid_letters:
                print('The first co-ordinate must be a letter A-J.')
            elif guess[1:] not in grid_numbers:
                print('Second co-ordinate must be a number 1-10.')
            elif guess in guesses:
                print('Grid location already fired upon, please select a new target.')
            else:
                valid = 1
                break
        except:
            print('Incorrect input, please try a new co-ordinate.\nFor example "D7"')

    print(f'\nDialing in on {guess}.\nLaunching missile...')
    return guess


def guess_conversion(guess):
    '''
    This function converts the user's validated guess into an integer
    between 11-110 so that it can be used on the grid.
    
    The functions obtains the ordinal value or the given letter and
    combines it with the number via string concatenation, before 
    converting into an integer.

    If the second co-ordinate is 10, then the ordinal value of the letter
    is multiplied by 10 as string concatenation would not work.
    '''
    ordinal = ord(guess[0]) - 64
    
    if guess[1:] == '10':
        converted_guess = (ordinal + 1) * 10
    else:
        converted_guess = int(f'{ordinal}{guess[1:]}')
    return converted_guess
    

def hit_or_miss(guess, guesses, hits, misses, ship_sunk, **ships_player):
    '''
    This function determines whether a guess results in a hit or a miss.

    List comprehension is used to compare whether a ship's entire list
    is contained within the 'hits' list. If True then the ship is
    returned empty and the hits are replaced with the 'ship_sunk' list
    to show a new character on the displayed grid.
    '''
    miss = 1
    for name, ship in ships_player.items():
        if guess_conversion(guess) in ship:
            hits.append(guess_conversion(guess))
            ship_sunk_check = [i in hits for i in ship]
            miss = 0

            if all(ship_sunk_check):
                ship_sunk.extend(ship)
                ship = []
                hits = [i for i in hits if i not in ship_sunk]
                miss = 0
                print(f'You sunk my {name.upper()}!')

    if miss == 1:
        misses.append(guess_conversion(guess))
    
    guesses.append(guess)
    print(f'Guesses: {len(guesses)}')
    
    return guesses, ships_player, hits, misses, ship_sunk


cpu_creation(**ships_player)

display_grid(**ships_player)

cpu_creation(**ships_cpu)

for i in range(100):
    guess = validate_guess(guesses)
    guess_conversion(guess)
    guesses_2, ships_cpu, hits_2, misses_2, ship_sunk_2 = hit_or_miss(guess, guesses, hits_2, misses_2, ship_sunk_2, **ships_cpu)
    display_grid(**ships_player)
    cpu_turn(guesses, hits, misses, ship_sunk, **ships_player)

    if len(ship_sunk) == 17:
        print('You sunk all the enemy ships, you win the game!')
        break
