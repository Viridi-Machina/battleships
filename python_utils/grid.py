#          Grid construction elements (Using unicode characters)              #
# ___________________________________________________________________________ #

from colorama import Fore, Style

reset = Style.RESET_ALL
water = Fore.LIGHTCYAN_EX
fire = Fore.YELLOW
player = Fore.LIGHTBLUE_EX
enemy = Fore.RED

# The game grid is constructed line-by-line in the display_grid() function.
#
# Because the Unicode characters chosen are larger than standard letters
# and the display was desired to be larger, empty spaces have been added
# to seperate each element during construction.
#
# As the goal is two simultaneously display two grids; one for the player and
# one for the opponent, some variables have been created with a 2-stage 
# process to improve readability and reduce overall line length.
#
# Colorama-imported colours are used to distinguish hits and misses from the
# board. Each coloured element has to be reset within their variable or the
# colour will be applied to everything else in the console.

grid_size = 10

vertical = f'{player}\u2503{reset}'
vertical_2 = f'{enemy}\u2503{reset}'
horizontal = '\u2501'*(33)

tl_corner = '\u250F'
tr_corner = '\u2513'
br_corner = '\u251B'
bl_corner = '\u2517'

spacer = ' '

# Empty circle for grid co-ordinates
grid = f'{water}\U0001F785{reset}{spacer}'

# Star indicate hit
hit = f'{fire}\U0001F7D2{reset}{spacer}'

# Cross to indicate miss
miss = f'{Fore.WHITE}\U0001F7AC{reset}{spacer}'

# Solid circle to display player ship or sunken enemy ship
ship_player_display = f'{player}\u2B24{reset}{spacer*2}'
sunk_2 = f'{enemy}\u2B24{reset}{spacer*2}'

# Circle with X to indicate hit on player
sunk_player = f'{player}\u2BBE{reset}{spacer*2}'

grid_title_player = f'\n{spacer*13}{player}PLAYER GRID{reset}'
grid_title_both = f'{grid_title_player}{spacer*31}{enemy}ENEMY GRID{reset}'

grid_top = f'{tl_corner}{horizontal}{tr_corner}'
grid_top_player = f'\n{spacer*2}{player}{grid_top}{reset}'
grid_top_both = f'{grid_top_player}{spacer*7}{enemy}{grid_top}{reset}'

grid_bottom = f'{spacer*2}{bl_corner}{horizontal}{br_corner}'
grid_bottom_player = f'{player}{grid_bottom}{reset}'
grid_bottom_both = f'{grid_bottom_player}{spacer*5}{enemy}{grid_bottom}{reset}'

grid_letters = ['A','B','C','D','E','F','G','H','I','J']
grid_numbers = ['1','2','3','4','5','6','7','8','9','10']
grid_numbers_string = spacer*3 + ''.join(f'{spacer*2}{i}' for i in range(1,11))
# The .join method converts the list comprehension into a string