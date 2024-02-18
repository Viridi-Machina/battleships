
def ask_to_reset():
    '''
    This function asks the player if they would like to play again,
    and returns either 1 or 0.
    '''
    valid = 0
    while valid == 0:
        choices = ['Y', 'N']
        try:
            manual_placement = input('Would you like to play again? Y / N\n')
            
            choice = manual_placement.upper().strip()

            if choice == '':
                print('\nPlease select either "Y" or "N" for an answer\n')
            elif choice not in choices:
                print('\nPlease select either "Y" or "N" for an answer\n')
            elif choice in choices:
                valid = 1

        except TypeError:
            print('\nIncorrect input, please try answering "Y" or "N"\n')
    
    if choice == 'Y':
        reset = 1
    elif choice == 'N':
        reset = 0

    return reset

def reset_game():
    '''
    This function resets the game by setting all stats to their initial values.
    '''
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
    aim = []
    missed = 0

    ships_cpu = {
        'cruiser': [2.0],
        'submarine': [3.0],
        'destroyer': [3.1],
        'battleship': [4.0],
        'aircraft_carrier': [5.0]
    }
