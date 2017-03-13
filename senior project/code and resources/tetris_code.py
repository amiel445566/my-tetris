########################################################################################
'''
IMMEDIATE TO DO's
- Set up current piece value and next pieces list (3 values; 2 displayed)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOON TO DO's:
- set up conditions for setting pieces down (copy from movement_map to placement_map)
    > *don't forget to not include 0's in the copying process*
- learn about importing time and it's functions
    > coordinate time with the visuals so render time doesnt add to cycle time

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
from random import *

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

""" movement_map differs from placement_map because it is used as
an overlay to the default map space such that there aren't any issues
with memory and piece locations as well as having the 0's in the piece
array overwrite used space """

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
current_piece = () # when setting use = deepcopy(piece[n])
next_pieces = [] # when setting, generate random values between 0 and 6 and generate 3 pieces with append

# map testing functions
def index_is_clear(map_index_list):
    """ tests the placement map at the given index to see if it is clear (a 0)  """

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
    else:
        return None # PLACE CODE FOR FAILURE HERE
    for i in movement_map: # FOR DEBUG, REMOVE LATER
        print(i)

def test_rows_filled():
    """ cycles through all rows in placement_map and returns
    a list of all row indecies that are filled """
    rows_filled = []
    for i in range(len(placement_map)):
        if 0 not in placement_map[i]:
            rows_filled.append(i)
    return rows_filled

def test_rows_nonzero(): # this function is used to minimize loops in row removal process
    """ cycles through all rows in placement_map and returns
    a list of all row indecies that aren't all zero values """
    rows_nonzero = []
    for i in range(len(placement_map)):
        if len(set(placement_map[i])) > 1 and 0 in placement_map[i]: # all nonzero lists without filled duplicates
            rows_nonzero.append(i)
    return rows_nonzero

def shift_row_down(row_index):
    """ takes the given row index and shifts the row down
    by one index in placement_map"""
    placement_map[row_index + 1] = placement_map[row_index]
    placement_map[row_index] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # empty current list to avoid copy error

def remove_filled_rows():
    """ removes filled rows and shifts the remaining
    blocks above, down """
    rows_filled = test_rows_filled()
    rows_nonzero = test_rows_nonzero()
    for i in range(len(test_rows_filled())): # empty filled rows
        placement_map[rows_filled[i]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if len(test_rows_nonzero()) > 0:
        rows_filled = rows_filled[::-1] # start from the top because top rows move down more; avoids stack count
        row_removed_count = 0
        while len(rows_filled) > 0: # loop for each row deletion (higher nonzero rows stack movements)
            for i in rows_nonzero: # non-reversed as to not override lower nonzero rows; rely on rows_filled[::-1]
                if i < rows_filled[0]:
                    shift_row_down(i + row_removed_count) # adjust for downward shifts to the row index
                else:
                    break
            row_removed_count += 1
            del rows_filled[0] # loop to lower rows and restart process until rows_filled empties
            
            

# BECAUSE YOU TEND TO FORGET THINGS (YOU IDIOT), HERES A DEMO FOR DOWNWARD MOVEMENT
#current_piece = deepcopy(pieces[0])
#for i in range(7):
#    if i == 3:
#        current_piece = rotate_clockwise(current_piece)
#    reset_map("movement_map")
#    place_piece(current_piece, (2+i, 3))
