########################################################################################
'''
IMMEDIATE TO DO's
- simplify movement
- set up main loop (create empty functions for missing pieces)
- print a series of lines with pygame timing every second or so (to learn timing)
- in the main loop structure, add timing_increase to all applicable states

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOON TO DO's:
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
from pygame import * # reinstall pygame to reenable function
from sys import *
from copy import *
from random import *

# GLOBAL VARIABLES
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

""" movement_map differs from placement_map because it is used as
an overlay to the default map space such that there aren't any issues
with memory and piece locations as well as having the 0's in the piece
array overwrite used space """

# VARIABLES
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

movement_piece_location = ()# initialize; stores indecies of piece on map; changes every transformation
current_piece = () # when setting use = deepcopy(piece[n])
next_pieces = [] # when setting, generate random values between 0 and 6 and generate 3 pieces with append
timing_increase = 1.0 # used to increase game speed over time (after n lines completed or something)
score = 0 # score added by scattered functions throughout (see the outline)

##############################################################################################
##################################### PIECE MODIFICATION #####################################
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

##############################################################################################
######################################## TRANSLATIONS ########################################
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
        return None # PLACE CODE FOR FAILURE HERE, EG place piece if the main loop is blocked when placing below
    for i in movement_map: # FOR DEBUG, REMOVE LATER
        print(i)

def shift_row_down(row_index):
    """ takes the given row index and shifts the row down
    by one index in placement_map"""
    placement_map[row_index + 1] = placement_map[row_index]
    placement_map[row_index] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # empty current list to avoid copy error

##############################################################################################
#################################### TESTS ###################################################
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

##############################################################################################
############################## GLOBAL MODIFICATION ###########################################
def reset_map(map_name="all"):
    """ resets the specified map:
    - placement_map
    - movement_map
    - all """
    value_reset = False
    if map_name == "placement_map" or map_name == "all":
        global placement_map
        placement_map = deepcopy(empty_map)
        value_reset = True
        print("reset placement_map") # FOR DEBUG, REMOVE LATER
    if map_name == "movement_map" or map_name == "all":
        global movement_map
        movement_map = deepcopy(empty_map)
        value_reset = True
        print("reset movement_map") # FOR DEBUG, REMOVE LATER
    if value_reset == False: # FOR DEBUG, REMOVE LATER
        print("map_name: '" + str(map_name) + "' unrecognized")

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
    score += (len(rows_filled) ** 2) * 10 * timing_increase # score += 10t(n^2), t = timing, n = rows

def piece_generation():
    """ generates and updates the variable that holds
    the next pieces """
    global next_pieces # access the global variable
    while len(next_pieces) < 3: # check length and update accordingly
        next_pieces.append(pieces[randint(0, 6)])

def reset_variable(var_name="all"):
    """ used to reset the variable named 'var_name'
    to its default value """
    value_reset = False
    if var_name == "movement_piece_location" or var_name == "all":
        movement_piece_location = ()
        value_reset = True
        print("reset movement_piece_location") # FOR DEBUG, REMOVE LATER
    if var_name == "current_piece" or var_name == "all":
        current_piece = ()
        value_reset = True
        print("reset current_piece") # FOR DEBUG, REMOVE LATER
    if var_name == "next_pieces" or var_name == "all":
        next_pieces = []
        value_reset = True
        print("reset next_pieces") # FOR DEBUG, REMOVE LATER
    if var_name == "timing_increase" or var_name == "all":
        timing_increase = 1.0
        value_reset = True
        print("reset timing_increase") # FOR DEBUG, REMOVE LATER
    if var_name == "score" or var_name == "all":
        score = 0
        value_reset = True
        print("reset score") # FOR DEBUG, REMOVE LATER
    if value_reset == False: # FOR DEBUG, REMOVE LATER
        print("var_name: '" + str(var_name) + "' unrecognized")
