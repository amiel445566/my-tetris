########################################################################################
'''
SOON TO DO's:
- clean up background highlight above
    > do this by testing column contents and determining if above is covered or not
- change favicon
- add in placement when down is denied
    > don't forget that diagonals may need different permissions
- add in UI
    > next pieces
        >> hold functionality? (if so, up/s/shift?)
    > learn to add text
    > score
        >> complete by adding:
            - manual down press (1t)
            - manual quick place (4nt)
            - all scaled by timing increase
    > lines completed
    > blocks placed (?)
    > clickable (learn how) button back to menu
    > alternatively, escape to open menu
- add in menu
    > clickable
    > keyboard select as well (?)
- prepare to add in SFX and BGM

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
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],
    [9, 8, 9, 8, 9, 8, 9, 8, 9, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
    ]

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

    [[6, 6, 6],
     [6, 0, 0]],

    [[7, 7, 7],
     [0, 0, 7]]
    ]

black                = (0  ,0  ,0  )
white                = (255,255,255)
red                  = (255,0  ,0  )
green                = (0  ,255,0  )
blue                 = (80 ,80 ,255)
orange               = (255,165,0  )
cyan                 = (0  ,255,255)
purple               = (188,65 ,234)
pink                 = (255,20 ,147)
light_gray           = (50 ,50 ,50 )
dark_gray            = (40 ,40 ,40 )
highlight_light_gray = (80 ,80, 80 )
highlight_dark_gray  = (65 ,65 ,65 )

color_key = {
    0:black,
    1:blue,
    2:red,
    3:green,
    4:orange,
    5:cyan,
    6:purple,
    7:pink,
    8:light_gray,
    9:dark_gray,
    10:highlight_light_gray,
    11:highlight_dark_gray
    }

current_piece_location = ()# initialize; stores indecies of piece on map; changes every transformation
current_piece = () # when setting use = deepcopy(piece[n])
next_pieces = [] # when setting, generate random values between 0 and 6 and generate 3 pieces with append
timing_increase = 1.0 # used to increase game speed over time (after n lines completed or something)
score = 0 # score added by scattered functions throughout (see the outline)

display_width = 200
display_height = 480
tile_size = 20 # size of each grid space

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
        current_piece_location = deepcopy(map_index_list)
        if update_current_piece:
            current_piece = deepcopy(piece)
        for i in range(len(piece)): # place piece in predetermined spot
            for j in range(len(piece[i])):
                movement_map[map_index_list[0] + i][map_index_list[1] + j] = piece[i][j]
    else: # PLACE CODE FOR FAILURE HERE, EG place piece if the main loop is blocked when placing below
        print("else block reached in place_movement_piece") # FOR DEBUG, REMOVE LATER
        main() # TAG: configure this more appropriately better

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
    global score
    
    rows_filled = test_rows_filled()
    score += (len(rows_filled) ** 2) * 10 * timing_increase # score += 10t(n^2), t = timing, n = rows

    print("rows filled: " + str(rows_filled))
    for i in range(len(test_rows_filled())): # empty filled rows
        placement_map[rows_filled[i]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    rows_nonzero = test_rows_nonzero()
    while len(rows_filled) > 0 and len(rows_nonzero) > 0:
        down_shift_index = max(rows_filled) # tells the loop where to begin shifting from
        for i in range(rows_filled[len(rows_filled) - 1] - rows_nonzero[0]):
            shift_row_down(down_shift_index - i - 1) # shift down each row above the lowest filled row
        del rows_filled[len(rows_filled) - 1] # remove the max value from rows filled as it has been completed already
        for i in (rows_filled, rows_nonzero): # add 1 to each index value
            for j in range(len(i)):
                i[j] = i[j] + 1

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
        # used for held repetition
    left_count = 0
    right_count = 0
    down_count = 0
    a_count = 0
    d_count = 0
    space_count = 0
    
        # used for confirmation of movement
    move_left = False
    move_right = False
    move_down = False
    move_c = False
    move_cc = False
    move_qp = False # move quick place

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
        if len(current_piece_location) == 0: # <- there isn't a current piece in the movement map
            if len(current_piece[0]) == 2: # <- and the 2 similar blocks below center placement
                place_movement_piece(current_piece, [0, 4])
            if len(current_piece[0]) == 3:
                place_movement_piece(current_piece, [0, 3])
            if len(current_piece[0]) == 4:
                place_movement_piece(current_piece, [0, 3])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # test for inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    left_pressed = True
                if event.key == pygame.K_KP6:
                    right_pressed = True
                if event.key == pygame.K_KP5:
                    down_pressed = True
                if event.key == pygame.K_a:
                    a_pressed = True
                if event.key == pygame.K_d:
                    d_pressed = True
                if event.key == pygame.K_SPACE:
                    space_pressed = True
            # remove boolean if key is let go
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_KP4:
                    left_pressed = False
                if event.key == pygame.K_KP6:
                    right_pressed = False
                if event.key == pygame.K_KP5:
                    down_pressed = False
                if event.key == pygame.K_a:
                    a_pressed = False
                if event.key == pygame.K_d:
                    d_pressed = False
                if event.key == pygame.K_SPACE:
                    space_pressed = False
        
        # deal with inputs TAG: change the 8 and 20 to be divided by timing_increase and rounded in directionals
        if left_pressed: # pulse once, and every 8th frame after 20 frames
            left_count += 1
            if left_count == 1:
                move_left = True
            elif left_count >= 15 and left_count % 5 == 0:
                move_left = True
            else:
                move_left = False
        else:
            left_count = 0
            move_left = False
        
        if right_pressed: # pulse once, and every 8th frame after 20 frames
            right_count += 1
            if right_count == 1:
                move_right = True
            elif right_count >= 15 and right_count % 5 == 0:
                move_right = True
            else:
                move_right = False
        else:
            right_count = 0
            move_right = False
        
        if down_pressed: # pulse once, and every 8th frame after 20 frames
            down_count += 1
            if down_count == 1:
                move_down = True
            elif down_count >= 15 and down_count % 5 == 0:
                move_down = True
            else:
                move_down = False
        else:
            down_count = 0
            move_down = False

        if a_pressed: # only single pulse
            a_count += 1
            if a_count == 1:
                move_cc = True
            else:
                move_cc = False
        else:
            a_count = 0
            move_cc = False

        if d_pressed: # only single pulse
            d_count += 1
            if d_count == 1:
                move_c = True
            else:
                move_c = False
        else:
            d_count = 0
            move_c = False
            
        if space_pressed: # only single pulse
            space_count += 1
            if space_count == 1:
                move_qp = True
            else:
                move_qp = False
        else:
            space_count = 0
            move_qp = False
        if move_qp:
            quick_place()
        if (move_left or move_right or move_down or move_cc or move_c) and not move_qp: # confirm movement
            move_current_piece(left=move_left,
                               right=move_right,
                               down=move_down,
                               rotate_cc=move_cc,
                               rotate_c=move_c)
        if move_right:
            print("moved right")
        if move_cc:
            print("rotated counter-clockwise")

        if test_rows_filled():
            remove_filled_rows()
        # draw the map
        for i in range(24): # first draw the background; highlight current piece columns
            for j in range(10):
                if len(current_piece_location) > 0 and j in range(current_piece_location[1], current_piece_location[1] + len(current_piece[0])):
                    pygame.draw.rect(gameDisplay,
                                     color_key[background_pattern[i][j] + 2],
                                     [j * tile_size, i * tile_size, tile_size, tile_size])
                else:
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
        clock.tick(60)
    
main()
