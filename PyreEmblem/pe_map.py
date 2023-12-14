import random as rand
import csv

global rows; rows = 3
global cols; cols = 3
global map_arr; map_arr = [[0 for i in range(cols)] for j in range(rows)]
# tile set below is defined as follows
#   each row is a tile definition
#   col 1 = tile name
#   col 2 = evasion bonus
#   col 3 = defense bonus
#   col 4 = resistance bonus
#   col 5 = heal per turn
#   col 6 = movement cost
global tile_set; tile_set = [['::', 0, 0, 0, 0, 0],      # floor
                             ['TR', 5, 1, 0, 0, 1],      # trees
                             ['MT', 20, 1, 1, 0, 4],     # mountain
                             ['FT', 12, 2, 2, 0, 0],     # fort
                             ['PK', 35, 1, 0, 0, 6],     # mountain peak
                             ['TH', 12, 2, 4, 4, 0],     # throne
                             ['CH', 10, 0, 1, 10, 0],    # church
                             ['WA', 0, 0, 0, 0, 99]]     # wall

# set global cols var
def set_cols(num):
    global cols; cols = num

# set global rows var
def set_rows(num):
    global rows; rows = num

# get global cols var
def get_cols():
    global cols; return cols

def get_rows():
    global rows; return rows

# return the zeroed array result of size c by r
def gen_map(c, r):
    global map_arr
    set_cols(c)
    set_rows(r)
    result = [[0 for i in range(c)] for j in range(r)]
    map_arr = result

def get_map():
    global map_arr; return map_arr

def get_tile(tile_ind):
    global tile_set
    if tile_ind < len(tile_set):
        return tile_set[tile_ind][0]
    else:
        return "~~"

# NEEDS: handle str elements
#       convert int indicies to tile strings
#       ensure strings/tiles are 2 char long
# print map_arr
def print_map():
    global map_arr
    # get dimensions of current map_arr
    w, h = (len(map_arr[0]), len(map_arr))
    #print(flush=True)          # flush console
    # print top border
    print('-', end=' ')
    for i in range(0, w):
        print('--', end=' ')
    print('-')
    # print array with leading + ending borders
    for i in range(0, h):
        print('|', end=' ')
        for j in range(0, w):
            print(get_tile(map_arr[i][j]), end=' ')
        print('|')
    # print bottom border
    print('-', end=' ')
    for i in range(0, w):
        print('--', end=' ')
    print('-')

def load_map(map_preset):
    # access current map
    global map_arr
    # get dimensions of map to load
    w, h = (len(map_preset[0]), len(map_preset))
    # reset current map
    gen_map(w, h)
    # copy each tile from loaded map to map_arr
    for i in range(0, h):
        for j in range(0, w):
            map_arr[i][j] = map_preset[i][j]

def csv_to_map():
    global map_arr
    try:
        with open('PyreEmblem\map_file.csv', newline='') as f:
            reader = csv.reader(f)
            map_arr = list(reader)
    except IOError:
        print("Error: could not open map_file")