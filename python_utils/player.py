
def player_creation_choice():
    '''
    This function asks the player if they would like to have their ships
    automatically generated or not, and returns their choice.
    '''
    valid = 0
    while valid == 0:
        choices = ['Y', 'N']
        try:
            manual_placement = input('Would you like to place'
                                     'your own ships? Y / N\n')
            
            choice = manual_placement.upper().strip()

            if len(choice) > 1:
                print('\nAnswer requires only one character\n')
            elif choice not in choices:
                print('\nPlease select either "Y" or "N" for an answer\n')
            elif choice in choices:
                valid = 1

        except TypeError:
            print('\nIncorrect input, please try answering "Y" or "N"\n')
    
    return choice

def player_creation(**ships_player):

    ship_start = input()