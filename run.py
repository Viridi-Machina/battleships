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

grid_size = 10 # Default grid-size; future implementation to alter based on user choice
# Unicode characters used for styling
grid = '\U0001F785  ' # Circle unicode character with space
# Grid border pieces
line_y = '\u2503 ' # Vertical border
line_x = '\u2501'*(3*grid_size + 3)  # Horizontal border
tl_corner = '\u250F'
tr_corner = '\u2513'
br_corner = '\u251B'
bl_corner = '\u2517'

# For loop to create grid that scales based on the set grid_size variable
print(f'\n  {tl_corner}{line_x}{tr_corner}')
grid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for i in range(grid_size):
    print(grid_letters[i], line_y, grid*grid_size, line_y)
print(f'  {bl_corner}{line_x}{br_corner}\n     1  2  3  4  5  6  7  8  9  10\n')