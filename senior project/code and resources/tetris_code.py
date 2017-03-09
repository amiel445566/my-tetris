########################################################################################
'''
TO DO:
note:   (these are some things that need to be completed next/soon)

- learn about importing time and it's functions
    > coordinate time with the visuals so render time doesnt add to cycle time
- set up conditions for setting pieces down (copy from movement_map to placement_map)
    > *don't forget to not include 0's in the copying process*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FINAL TO DO's:
note:   (list MAY be incomplete)
        (some elements MAY be completed before the final product)

- remove debug tools
- remove ASCII map prints
- create a game loop (*reference the game state machine*)
- turn into an EXE
'''
########################################################################################

# import statements
'''from pygame import *''' # reinstall pygame to reenable function
from sys import *
from copy import *

# global variables
empty_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

# initialize maps
placement_map = deepcopy(empty_map)
movement_map = deepcopy(empty_map)

def reset_map(map_name):
    """ resets the specified map:
    - placement_map
    - movement_map
    - all """
    if map_name == "placement_map" or map_name == "all":
        global placement_map
        placement_map = deepcopy(empty_map)
        print("placement_map reset") # FOR DEBUG, REMOVE LATER
    if map_name == "movement_map" or map_name == "all":
        global movement_map
        global movement_piece_location
        movement_map = deepcopy(empty_map)
        movement_piece_location = () # because the piece gets removed, so should its location
        print("movement_map reset") # FOR DEBUG, REMOVE LATER
    else: # FOR DEBUG, REMOVE LATER
        print("map_name: '" + str(map_name) + "' unrecognized")

''' movement_map differs from placement_map because it is used as
an overlay to the default map space such that there aren't any issues
with memory and piece locations as well as having the 0's in the piece
array overwrite used space '''

pieces = [
    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 3],
     [0, 3, 0]],

    [[4, 4],
     [4, 4]],

    [[5, 5, 5, 5]],

    [[6, 6, 6, 6],
     [6, 0, 0, 0]],

    [[7, 7, 7, 7],
     [0, 0, 0, 7]]
    ]

# initialize; stores indecies of piece on map; changes every transformation
movement_piece_location = ()

# piece modification functions
def rotate_clockwise(piece):
    new_piece = [] # placeholder for the new piece state
    for i in list(range(len(piece[0]))):
        temp_list = [] # used for generating new multidimensional rows
        for j in list(range(len(piece)))[::-1]:
            temp_list.append(piece[j][i])
        new_piece.append(temp_list) # insert current row to new state
    return new_piece

def rotate_counterclockwise(piece): # *see clockwise notes*
    new_piece = []
    for i in list(range(len(piece[0])))[::-1]:
        temp_list = []
        for j in list(range(len(piece))):
            temp_list.append(piece[j][i])
        new_piece.append(temp_list)
    return new_piece

def place_piece(piece, map_index_list):
    """ places piece at movement_map[map_index_list] where
    map_index_list = (24-y, 10-x) """
    global movement_piece_location
    movement_piece_location = deepcopy(map_index_list)
    placement_clear = True # allows placement to begin if map underneath is clear
    for i in range(len(piece)): # first test if the map underneath is clear
        for j in range(len(piece[i])):
            if placement_map[map_index_list[0] + i][map_index_list[1] + j] != 0 and piece[i][j] != 0:
                placement_clear = False
                print("placement blocked at location: (" + # FOR DEBUG, REMOVE LATER
                      str(map_index_list[1] + j + 1) +
                      ", " + str(24 - (map_index_list[0] + i)) +
                      ")")
    if placement_clear:
        for i in range(len(piece)): # place piece in predetermined spot
            for j in range(len(piece[i])):
                movement_map[map_index_list[0] + i][map_index_list[1] + j] = piece[i][j]
    for i in movement_map: # FOR DEBUG, REMOVE LATER
        print(i)
    else:
        return None # PLACE CODE FOR FAILURE HERE
# BECAUSE YOU TEND TO FORGET THINGS (YOU IDIOT), HERES A DEMO FOR DOWNWARD MOVEMENT
#for i in range(7):
#    reset_map("movement_map")
#   place_piece(pieces[0], (2+i, 3))
