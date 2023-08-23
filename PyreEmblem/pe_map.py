import random as rand

global rows; rows = 3
global cols; cols = 3
global map_arr; map_arr = [[0 for i in range(cols)] for j in range(rows)]


# set global cols var
def set_cols(num):
    global cols; cols = num

# set global rows var
def set_rows(num):
    global rows; rows = num

# return the zeroed array result of size c by r
def gen_map(c, r):
    global map_arr
    set_cols(c)
    set_rows(r)
    result = [[0 for i in range(c)] for j in range(r)]
    map_arr = result

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
            if map_arr[i][j] < 10:
                print("0" + str(map_arr[i][j]), end=' ')
            else:
                print(map_arr[i][j], end=' ')
        print('|')
    # print bottom border
    print('-', end=' ')
    for i in range(0, w):
        print('--', end=' ')
    print('-')