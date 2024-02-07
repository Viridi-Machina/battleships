# The following code is mostly adapted from a python code tutorial video-series 
# from 'Dr Codie' on YouTube: https://www.youtube.com/@DrCodie

from random import randrange
import math



def validate_placement(ship, start, direction, **ships_cpu):
    '''
    This function uses the randomly generated starting points and directions 
    for each ship to determine grid co-ordinates for each ship in the
    dictionary, before returning that dictionary for use in the game loop.

    With how each dictionary value is used first as a comparitor with the 
    ship argument, new values are appended first rather than redefining an
    empty list. Then the first element of each list is removed.

    '+/- i' adds a co-ordinate horizontally.
    '+/- i*10' adds a co-ordinate vertically.
    '''
    
    for x in ships_cpu.values():

        if direction == 1:
            if ship == x[0]:
                for i in range(math.floor(ship)):
                    x.append(start - i*10)
                x.remove(x[0])

        elif direction == 2:
            if ship == x[0]:
                for i in range(math.floor(ship)):
                    x.append(start + i)
                x.remove(x[0])

        elif direction == 3:
            if ship == x[0]:
                for i in range(math.floor(ship)):
                    x.append(start + i*10)
                x.remove(x[0])

        elif direction == 4:
            if ship == x[0]:
                for i in range(math.floor(ship)):
                    x.append(start - i*10)
                x.remove(x[0])



      
ships_cpu = {
    'cruiser': [2.0],
    'submarine': [3.0],
    'destroyer': [3.1],
    'battleship': [4.0],
    'aircraft_carrier': [5.0]
}
def cpu_placement():
    '''
    This function uses random number generation to assign assign co-ordinates
    for the computer's ships on the grid. It returns a dictionary which is
    used for the hit_or_miss() function during the game loop.

    Floats are used to identify the different key-values in the ships_cpu
    dictionary as two keys would otherwise both have a value of [3].
    This stops the validate_placement() function from overwriting the 
    'destroyer' value with that of the 'submarine'.

    The directions 1-4 are equal to up, right, down and left respectively.
    '''
    computer_ships = [2.0, 3.0, 3.1, 4.0, 5.0]
    for ship in computer_ships:
        ship_start_grid = randrange(11, 110)
        ship_direction = randrange(1,5)

        validate_placement(ship, ship_start_grid, ship_direction, **ships_cpu)
    print(ships_cpu)

cpu_placement()
# for x in ships_cpu.values():
#     print(x)