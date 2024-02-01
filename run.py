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

from colorama import Fore

grid_size = 10 # Default grid-size; future implementation to alter based on user choice

# Unicode characters used for border styling
# Grid border pieces
line_y = '\u2503 ' # Vertical border
line_x = '\u2501'*(3*grid_size + 3)  # Horizontal border
tl_corner = '\u250F'
tr_corner = '\u2513'
br_corner = '\u251B'
bl_corner = '\u2517'
hit = '\U0001F7D2  '
miss = '\U0001F7AC  '

def display_grid(hits,misses):
    '''
    This function displays the updated grid for the player; 
    showing any hits and misses on the board.

    Two for loops create a grid that scales based on the defined grid_size variable.
    'grid_row = grid_row + grid_element' adapted from python code from a tutorial video 
    from 'Dr Codie' on YouTube: https://www.youtube.com/@DrCodie
    '''
    # Forms grid top
    print(f'\n  {tl_corner}{line_x}{tr_corner}')
    grid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    # Forms grid body
    grid_location = 11 # Starts at 11 as the grid numbering starts from 1,1 (A1)
    for x in range(grid_size):
        grid_row = ''
        for y in range(grid_size):
            grid_element = '\U0001F785  ' # Circle unicode character with space
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
misses = [13,14,15]
display_grid(hits,misses)