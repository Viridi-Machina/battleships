# The following code is mostly adapted from a python code tutorial video-series
# from 'Dr Codie' on YouTube: https://www.youtube.com/@DrCodie

from colorama import Fore, Style

from random import randrange
import math
import time


def validate_placement(ship, start, direction, in_use):
    '''
    This function uses the randomly generated starting points and directions
    for each ship to determine their grid co-ordinates.

    A helper function ship_valid() checks whether new co-ordinates are legal
    and returns the ship (x) as [-1] to continue the cpu_creation loop.

    '+ i' adds a co-ordinate horizontally.
    '+ i*10' adds a co-ordinate vertically.
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
    This helper function validates whether the assigned ship co-ordinates are
    'legal', specifically checking if any co-ordinates are:

    - Already used by another ship
    - Outside the grid scope
    - Finishing on another row
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


def cpu_creation(**ships_cpu):
    '''
    This function uses random number generation to assign co-ordinates
    for the computer's ships on the grid.

    Each ship is created through a loop
    and is stored in both [computer_ships] and [in_use] (for validation).
    Then the dictionary is returned with the new ships for the hit_or_miss()
    function during the main game loop.

    Floats are used to identify the different key-values in the ships_cpu
    dictionary as two keys would otherwise both have a value of [3].
    This stops the validate_placement() function from overwriting the
    'destroyer' value with that of the 'submarine'.

    The directions '1' & '2' are equivalent to 'right' & 'down' respectively.
    '''
    in_use = []
    computer_ships = []
    ship_index = [2.0, 3.0, 3.1, 4.0, 5.0]

    for ship in ship_index:
        x = [-1]
        while x[0] == -1:
            ship_start_grid = randrange(11, 110)
            ship_direction = randrange(1, 3)

            x = validate_placement(ship, ship_start_grid,
                                   ship_direction, in_use)

        computer_ships.append(x)
        in_use = in_use + x

    for list in ships_cpu.values():
        for ship in computer_ships:
            if ship[0] == list[0]:
                list.remove(list[0])
                ship.remove(ship[0])
                list.extend(ship)

    return ships_cpu


def cpu_turn(guesses, hits, misses, ship_sunk, aim, missed, **ships_player):
    '''
    This function is a modified version of the hit_or_miss function,
    for use by the computer when it takes it's turn.

    It a random shot generator as well as a modified print message when
    when one of the player's ships has been sunk.
    '''
    valid = 'N'
    while valid == 'N':
        if len(aim) > 0:
            target = aim[randrange(len(aim))]
        else:
            target = randrange(11, 110)

        if target not in guesses:
            valid = 'Y'
            guesses.append(target)

    missed = 1
    for name, ship in ships_player.items():
        if target in ship:
            hits.append(target)
            ship_sunk_check = [i in hits for i in ship]
            missed = 0
            print(f'{Fore.YELLOW}We just took a hit!{Style.RESET_ALL}')
            time.sleep(1)

            if all(ship_sunk_check):
                ship_sunk.extend(ship)
                ship = []
                hits = [i for i in hits if i not in ship_sunk]
                missed = 2
                print(f'We just lost our {Fore.LIGHTBLUE_EX}'
                      f'{name.upper()}{Style.RESET_ALL}!')
                time.sleep(2)

    if missed == 1:
        misses.append(target)

    if len(aim) > 0:
        aim.remove(target)

    return guesses, ships_player, hits, misses, ship_sunk, missed


def cpu_assist(aim, guesses, hits):
    '''
    This function acts as the computer logic for tactical firing.
    It takes guesses, compares with hits and adds new potential
    shots to the que if they are in the same direction as a ship
    that has already been hit.

    As the hits list is automatically overwritten on ship completion
    the computer should display relatively 'smart' thinking.
    '''
    potential = []
    logic = []
    for i in range(len(guesses)):
        if len(hits) <= 1:
            break

        # If there are adjacent hits on the board, the following
        # code creates potential shots in the correct direction.
        if guesses[i] in hits and guesses[i] + 1 in hits:
            logic.append(guesses[i] - 1)
        if guesses[i] in hits and guesses[i] + 10 in hits:
            logic.append(guesses[i] - 10)
        if guesses[i] in hits and guesses[i] - 1 in hits:
            logic.append(guesses[i] + 1)
        if guesses[i] in hits and guesses[i] - 10 in hits:
            logic.append(guesses[i] + 10)

    target = guesses[-1]
    try_again = 'Y'
    while try_again == 'Y':
        # On hit, expands on the most recent guess
        if len(logic) > 0:
            pass
        elif len(aim) < 1:
            logic = [target - 1, target + 1, target - 10, target + 10]

        # Validates and checks if future guesses are legal
        for j in range(len(logic)):
            if logic[j] not in guesses and logic[j] > 11 and logic[j] <= 110:
                potential.append(logic[j])
        try:
            if (target - 1) % 10 == 0:
                potential.remove(target - 1)
            if (target + 1) % 10 == 1:
                potential.remove(target + 1)
        except ValueError:
            pass

        if len(hits) >= 1 and potential == []:
            target = hits[randrange(len(hits))]
            logic = []
            try_again = 'Y'
        else:
            try_again = 'N'

    return potential
