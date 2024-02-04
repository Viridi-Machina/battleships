# FUNCTION Launch Game
# Welcome Screen
# INPUT Enter UserName
# Store UserName
# SELECT BOARD SIZE
# Show Board
# SELECT SHIP PLACEMENT
# Show Board

# START BATTLESHIPS
# Show Board
# INPUT Enter Guess
# VALIDATE Guess
# Guess already taken?
# - Within board scope?
# - Hit / miss / sink?
# - Offer feedback?

# Track score and save user email for login, store score and user information on external sheet
# With enough time, allow import from external sheet (with link for users) to import ship placement

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

grid = '\U0001F785  ' # Circle unicode character with space
hit = '\U0001F7D2  '  # Star unicode character to indicate hit
miss = '\U0001F7AC  ' # Cross unicode character to indicate miss

def display_grid(hits,misses):
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
    # grid_numbers = [1,2,3,4,5,6,7,8,9,10]

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
            grid_row = grid_row + grid_element
            grid_location = grid_location + 1
        print(grid_letters[x], line_y, grid_row, line_y)

    # Forms grid bottom
    print(f'  {bl_corner}{line_x}{br_corner}\n     1  2  3  4  5  6  7  8  9  10\n')

hits = [11,21,31]
misses = [13,14,15,23,54,52,51,34,32]
display_grid(hits,misses)

def validate_guess():
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

    valid = 0
    while valid == 0:
        try:
            guess = input('Select a co-ordinate to launch a missile: \n')
            if str.isalpha(guess[0]) == False:
                print('First co-ordinate must be a letter A-J.')
            elif guess[0].upper() not in grid_letters:
                print('The first co-ordinate must be a letter A-J.')
            elif guess[1:] not in grid_numbers:
                print('Second co-ordinate must be a number 1-10.')
            else:
                valid = 1
                break
        except:
            print('Incorrect input, please try a new co-ordinate.\nFor example "D7"')

    print(guess.upper())

validate_guess()