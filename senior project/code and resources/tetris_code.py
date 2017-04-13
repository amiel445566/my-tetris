########################################################################################
'''
IMMEDIATE TO DO's
- begin the implemenetation of scoring
    > 1 point per grid space skipped
    > 2 points per grid space skipped in quick place
    > 10(n^2) points per line completed where n is lines completed in a turn
    > scale all score by timing_increase (as timing and score scale in tandem)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOON TO DO's:
- set up conditions for setting pieces down (copy from movement_map to placement_map)
    > *don't forget to not include 0's in the copying process*
- set up main loop (create empty functions for missing pieces)
- print a series of lines with pygame timing every second or so (to learn timing)
- in the main loop structure, add timing_increase to all applicable states
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
import pygame
from sys import *
from copy import *
from random import *

# GLOBAL VARIABLES
background_pattern = [
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 8, 0, 8, 0, 8, 0, 8, 0, 8],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0]
    ]

empty_map = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 3, 4, 5, 6, 7, 0, 0, 5]
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

black     = (0  ,0  ,0  )
white     = (255,255,255)
red       = (255,0  ,0  )
green     = (0  ,255,0  )
blue      = (0  ,0  ,255)
orange    = (255,165,0  )
cyan      = (0  ,255,255)
purple    = (153,50 ,204)
pink      = (255,20 ,147)
dark_grey = (50 ,50 ,50 )

color_key = {
    0:black,
    1:blue,
    2:red,
    3:green,
    4:orange,
    5:cyan,
    6:purple,
    7:pink,
    8:dark_grey
    }

current_piece_location = ()# initialize; stores indecies of piece on map; changes every transformation
current_piece = () # when setting use = deepcopy(piece[n])
next_pieces = [] # when setting, generate random values between 0 and 6 and generate 3 pieces with append
timing_increase = 1.0 # used to increase game speed over time (after n lines completed or something)
score = 0 # score added by scattered functions throughout (see the outline)

display_width = 250
display_height = 600
tile_size = 25 # size of each grid space

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tetris by Amiel Iliesi 2017')
clock = pygame.time.Clock()

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
def place_movement_piece(piece, map_index_list, update_current_piece=False):
    """ places piece at movement_map[map_index_list] where
    map_index_list = (24-y, 10-x),
    update_current_piece is useful for when the parameter is
    a modified version of the piece and updating is needed"""
    global current_piece
    global current_piece_location

    if test_if_clear(piece, map_index_list):
        if update_current_piece:
            current_piece = deepcopy(piece)
            current_piece_location = deepcopy(map_index_list)
        for i in range(len(piece)): # place piece in predetermined spot
            for j in range(len(piece[i])):
                movement_map[map_index_list[0] + i][map_index_list[1] + j] = piece[i][j]
    else: # PLACE CODE FOR FAILURE HERE, EG place piece if the main loop is blocked when placing below
        print("else block reached in place_movement_piece") # FOR DEBUG, REMOVE LATER
    for i in movement_map: # FOR DEBUG, REMOVE LATER
        print(i)

def shift_row_down(row_index):
    """ takes the given row index and shifts the row down
    by one index in placement_map"""
    placement_map[row_index + 1] = placement_map[row_index]
    placement_map[row_index] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # empty current list to avoid copy error

def move_current_piece(left=False, down=False, right=False, rotate_cc=False, rotate_c=False):
    """ takes a boolean directonal input and moves the piece
    one unit in that direction """

    global current_piece_location
    global current_piece
    global movement_map

    print("moving the piece from: " + str(current_piece_location)) # FOR DEBUG, REMOVE LATER

    # first, deal with duplicate and opposite directions
    if left and right:
        print("can't move left AND right, failed to move")
        return None
    elif rotate_c and rotate_cc:
        print("can't rotate left AND right, failed to rotate")
        return None
    
    # second, clear the map
    if test_if_clear(rotate_clockwise(current_piece) * rotate_c \
                           + rotate_counterclockwise(current_piece) * rotate_cc \
                           + current_piece * (not rotate_c and not rotate_cc),
                           [current_piece_location[0] + down,
                            current_piece_location[1] + right - left]):
        reset_map("movement_map")
    else:
        return None

    # third, translate current coordinates
        # places piece with function input modifications
    place_movement_piece(rotate_clockwise(current_piece) * rotate_c \
                         + rotate_counterclockwise(current_piece) * rotate_cc \
                         + current_piece * (not rotate_c and not rotate_cc),
                         [current_piece_location[0] + down,
                          current_piece_location[1] + right - left],
                         True)
    print("to: " + str(current_piece_location)) # FOR DEBUG, REMOVE LATER

def quick_place():
    """ places the current piece at the lowest vertical position possible """

    global current_piece
    global current_piece_location
    
    for i in range(1, 25): # places piece one before current piece is blocked (lowest possible)
        if not test_if_clear(current_piece, [current_piece_location[0] + i, current_piece_location[1]]):
            confirm_placement([current_piece_location[0] + i - 1, current_piece_location[1]])
            break
        

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

def test_if_clear(piece, map_index_list):
    # first, text map bounds with piece and given index
    if (map_index_list[0] < 0) or \
    (map_index_list[1] < 0) or \
    (map_index_list[0] + len(piece) - 1 > 23) or \
    (map_index_list[1] + (len(piece[0]) - 1) > 9):
        print("index out of range at: " + str(map_index_list) + " with piece: ") # FOR DEBUG, REMOVE LATER
        for i in piece: # FOR DEBUG, REMOVE LATER
            print(i)
        return False
    # second, test if the map below movement is clear
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if placement_map[map_index_list[0] + i][map_index_list[1] + j] != 0 and piece[i][j] != 0:
                print("placement blocked at location: (" + # FOR DEBUG, REMOVE LATER
                      str(map_index_list[1] + j + 1) +
                      ", " + str(24 - (map_index_list[0] + i)) +
                      ")")
                return False
    return True # only outputs if no other Falses are triggered earlier; test success indicator

##############################################################################################
############################## GLOBAL MODIFICATION ###########################################
def confirm_placement(map_index_list):
    """ places the current piece onto the placement map """

    global current_piece
    global next_pieces
    global placement_map
    
    if test_if_clear(current_piece, map_index_list):
        for i in range(len(current_piece)): # place piece in predetermined spot
            for j in range(len(current_piece[i])):
                if current_piece[i][j] == 0:
                    continue # stops the loop from finishing to prevent 0's from placing
                placement_map[map_index_list[0] + i][map_index_list[1] + j] = current_piece[i][j]
        # wipe the current turns' variables clean
        current_piece = next_pieces.pop(0)
        piece_generation()
        reset_map("movement_map")
        reset_variable("current_piece_location")
    else: # PLACE CODE FOR FAILURE HERE, EG place piece if the main loop is blocked when placing below
        print("else block reached in confirm_placement") # FOR DEBUG, REMOVE LATER

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

    global next_pieces
    global current_piece

    while len(next_pieces) < 3 or len(current_piece) < 0:
        while len(next_pieces) < 3: # check length and update accordingly
            next_pieces.append(pieces[randint(0, 6)])
        if len(current_piece) < 1: # fill current piece if empty with first index in next_pieces
            current_piece = next_pieces.pop(0)
            next_pieces.append(pieces[randint(0, 6)])

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

def reset_variable(var_name="all"):
    """ used to reset the variable named 'var_name'
    to its default value """

    global current_piece_location
    global current_piece
    global next_pieces
    global timing_increase
    global score

    value_reset = False
    
    if var_name == "current_piece_location" or var_name == "all":
        current_piece_location = ()
        value_reset = True
        print("reset current_piece_location") # FOR DEBUG, REMOVE LATER
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
    
##############################################################################################
##############################################################################################
######################################### MAIN START #########################################

""" note: pseudo code will be commented out because main functions aren't all yet completed;
          this just gives me a framework to work off of """

# define the function for looping
def main():
    """ call this function to start the application """
    # local variables to the game instance
    left_pressed = False
    right_pressed = False
    down_pressed = False
    a_pressed = False # rotate counterclockwise
    d_pressed = False # rotate clockwise
    space_pressed = False # quick place
    
    # add a menu in later
    
    # reset all variables
    reset_map("all")
    reset_variable()
    piece_generation()
    print("current piece:")
    for i in current_piece: # FOR DEBUG, REMOVE LATER
        print(i)
    print("next pieces:")
    for i in next_pieces: # FOR DEBUG, REMOVE LATER
        for j in i:
            print(j)

    # begin game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                if event.key == pygame.K_RIGHT:
                    right_pressed = True
                if event.key == pygame.K_DOWN:
                    down_pressed = True
                if event.key == pygame.K_a:
                    a_pressed = True
                if event.key == pygame.K_d:
                    d_pressed = True
                if event.key == pygame.K_SPACE:
                    space_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pressed = False
                if event.key == pygame.K_RIGHT:
                    right_pressed = False
                if event.key == pygame.K_DOWN:
                    down_pressed = False
                if event.key == pygame.K_a:
                    a_pressed = False
                if event.key == pygame.K_d:
                    d_pressed = False
                if event.key == pygame.K_SPACE:
                    space_pressed = False
        if right_pressed:
            print("right pressed")
        if left_pressed:
            print("left pressed")
        if down_pressed:
            print("down pressed")
        if a_pressed:
            print("a pressed")
        if d_pressed:
            print("d pressed")
        if space_pressed:
            print("space pressed")
        
        # draw the map
        for i in range(24): # first draw the background
            for j in range(10):
                pygame.draw.rect(gameDisplay,
                                 color_key[background_pattern[i][j]],
                                 [j * tile_size, i * tile_size, tile_size, tile_size])
        for i in range(24): # next draw both maps on top
            for j in range(10):
                for k in range(2): # k used to alternate between placement_map and movement_map
                    if k == 0:
                        if placement_map[i][j] != 0:
                            pygame.draw.rect(gameDisplay,
                                             color_key[placement_map[i][j]],
                                             [j * tile_size, i * tile_size, tile_size, tile_size])
                    else:
                        if movement_map[i][j] != 0:
                            pygame.draw.rect(gameDisplay,
                                             color_key[movement_map[i][j]],
                                             [j * tile_size, i * tile_size, tile_size, tile_size])

        # update the frame
        pygame.display.update()
        clock.tick(30)
    
