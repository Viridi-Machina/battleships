# The following code is mostly adapted from a python code tutorial video-series 
# from 'Dr Codie' on YouTube: https://www.youtube.com/@DrCodie

from random import randrange
import math



def validate_placement(ship, start, direction, in_use):
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
    
    x = [ship]
    if direction == 1:
        for i in range(math.floor(ship)):
            x.append(start + i)
        x = ship_valid(x, in_use)
    elif direction == 2:
        for i in range(math.floor(ship)):
            x.append(start + i*10)
        x = ship_valid(x, in_use)
    return x

def ship_valid(x, in_use):
    '''
    This helper function is a final validator to ensure that the assigned
    ship co-ordinates are 'legal'. I.e no overlapping, spreading from one 
    side of the grid to the other or placing outside the grid scope.
    '''
    for i in range(len(x)):
        co_ord = x[i]
        if co_ord in in_use:
            x = [-1]
            break
        if co_ord > 110:
            x = [-1]
            break
        elif co_ord % 10 == 0 and i < len(x)-1:
            if x[i+1] % 10 == 1:
                x = [-1]
                break
    return x


      
ships_cpu = {
    'cruiser': [2.0],
    'submarine': [3.0],
    'destroyer': [3.1],
    'battleship': [4.0],
    'aircraft_carrier': [5.0]
}

def cpu_creation(**ships_cpu):
    '''
    This function uses random number generation to assign assign co-ordinates
    for the computer's ships on the grid. It returns a dictionary which is
    used for the hit_or_miss() function during the game loop.

    Floats are used to identify the different key-values in the ships_cpu
    dictionary as two keys would otherwise both have a value of [3].
    This stops the validate_placement() function from overwriting the 
    'destroyer' value with that of the 'submarine'.

    The directions 1 & 2 are equal to right & down respectively.
    '''
    in_use = []
    computer_ships = []
    ship_index = [2.0, 3.0, 3.1, 4.0, 5.0]
    
    for ship in ship_index:
        x = [-1]
        while x[0] == -1:
            ship_start_grid = randrange(11, 110)
            ship_direction = randrange(1,3)

            x = validate_placement(ship, ship_start_grid, ship_direction, in_use)
            
        
        computer_ships.append(x)
        in_use = in_use + x

    for list in ships_cpu.values():
        for ship in computer_ships:
            if ship[0] == list[0]:
                list.remove(list[0])
                ship.remove(ship[0])
                list.extend(ship)

    return ships_cpu

cpu_creation(**ships_cpu)
print(ships_cpu)