# Player and computer score-cards used for keeping track of ship locations,
# guesses and other elements which influence the display_grid() function.

# Player score-card
hits_2 = []
misses_2 = []
guesses_2 = []
ship_sunk_2 = []

ships_player = {
    'cruiser': [2.0],
    'submarine': [3.0],
    'destroyer': [3.1],
    'battleship': [4.0],
    'aircraft_carrier': [5.0]
}

# Computer score-card
hits = []
misses = []
guesses = []
ship_sunk = []

ships_cpu = {
    'cruiser': [2.0],
    'submarine': [3.0],
    'destroyer': [3.1],
    'battleship': [4.0],
    'aircraft_carrier': [5.0]
}