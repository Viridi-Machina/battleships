# FUNCTION Launch Game
# Welcome Screen
# INPUT Enter UserName
# Store UserName
# SELECT BOARD SIZE
# Show Board
# SELECT SHIP PLACEMENT
# Show Board

# Track score and save user email for login, store score and user information on external sheet
# With enough time, allow import from external sheet (with link for users) to import ship placement

from typing import Any
from colorama import Fore, Style

# Default grid-size; future implementation to alter based on user choice
grid_size = 10 

# Unicode characters used for border styling.
# Grid border pieces:
line_y = '\u2503 ' # Vertical border
line_x = '\u2501'*(3*grid_size + 3)  # Horizontal border
tl_corner = '\u250F'
tr_corner = '\u2513'
br_corner = '\u251B'
bl_corner = '\u2517'

    # colorama-imported colours are used to distinguish hits 
    # and misses from the board.
    # The string is ended with {Fore.WHITE} so that the rest 
    # of the display remains unchanged.

grid = '\U0001F785  ' # Circle unicode character with space U0001F785
hit = '\U0001F7D2  '  # Star unicode character to indicate hit
miss = '\U0001F7AC  ' # Cross unicode character to indicate miss
sunk = '\u23FA  ' # Solid circle unicode character to indicate sunken ship

def display_grid(hits, misses, ship_sunk):
    '''
    This function displays the updated grid for the player; 
    showing any hits and misses on the board.

    Two for loops create a grid that scales based on the defined 
    grid_size variable.
    Adapted from a python code tutorial video-series from 
    'Dr Codie' on YouTube: https://www.youtube.com/@DrCodie
    '''
    # Forms grid top
    print(f'\n  {tl_corner}{line_x}{tr_corner}')
    grid_letters = ['A','B','C','D','E','F','G','H','I','J']

    # Forms grid body
    grid_location = 11 # Starts at 11 as the grid numbering starts from 1,1 (A1)
    for x in range(grid_size):
        grid_row = ''
        for y in range(grid_size):
            grid_element = grid 
            if grid_location in misses:
                grid_element = miss
            elif grid_location in hits:
                grid_element = hit
            elif grid_location in ship_sunk:
                grid_element = sunk
            grid_row = grid_row + grid_element
            grid_location = grid_location + 1
        print(grid_letters[x], line_y, grid_row, line_y)

    # Forms grid bottom
    print(f'  {bl_corner}{line_x}{br_corner}\n     1  2  3  4  5  6  7  8  9  10\n')


def validate_guess(guesses):
    '''
    This function validates that the user's guess is between A1 and J10
    and has not already been used.
    
    After validation the inputed guess will be converted into an uppercase 
    letter and number. Then the letter's ordinal value is combined with
    the given number to form a string, which is converted into a final
    integer that can be used to determine the shot location on the grid.
    '''

    grid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    grid_numbers = ['1','2','3','4','5','6','7','8','9','10']
    #guesses = ['D8', 'B9', 'C9', 'D9']

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
    for key, ship in ships_player.items():
        if guess_conversion(guess) in ship:
            hits.append(guess_conversion(guess))
            ship_sunk_check = [i in hits for i in ship]
            miss = 0

            if all(ship_sunk_check):
                ship_sunk.extend(ship)
                ship = []
                hits = [i for i in hits if i not in ship_sunk]
                miss = 0
                print(f'You sunk my {key.upper()}!')

    if miss == 1:
        misses.append(guess_conversion(guess))
    
    guesses.append(guess)
    print(f'Guesses: {len(guesses)}')
    
    return guesses, ships_player, hits, misses, ship_sunk

# Stores all ships on the board in a dictionary for reference
ships_player = {
    'cruiser': [92,93],
    'submarine': [110,100,90],
    'destroyer': [58,68,78],
    'battleship': [12,13,14,15],
    'aircraft_carrier': [21,22,23,24,25]
}


hits = []
misses = []
guesses = []
ship_sunk = []

for i in range(20):
    guess = validate_guess(guesses)
    guess_conversion(guess)
    guesses, ships_player, hits, misses, ship_sunk = hit_or_miss(guess, guesses, hits, misses, ship_sunk, **ships_player)
    display_grid(hits, misses, ship_sunk)

    if len(ship_sunk) == 17:
        print('You sunk all the enemy ships, you win the game!')
        break