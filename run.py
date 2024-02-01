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


# Unicode characters used for styling
grid = '\U0001F785  ' # Circle unicode character with space
# Grid border pieces
line_y = '\u2503 ' # Vertical border
line_x = '\u2501'*33  # Horizontal border
tl_corner = '\u250F'
tr_corner = '\u2513'
br_corner = '\u251B'
bl_corner = '\u2517'

# For loop to create default 10*10
grid_size = 10 # Default grid-size, to be altered with user choice
print(f'{tl_corner}{line_x}{tr_corner}')
for i in range(grid_size):
    print(line_y, grid*grid_size, line_y)
print(f'{bl_corner}{line_x}{br_corner}')