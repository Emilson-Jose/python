# made with Python 3.10.11

import random as rand
import subprocess as subp
import os

global var1; var1 = 0
global momba; momba = "Monday"

def hit_calc(a_spd, a_hit, d_avd):
    result = 0
    return result

def rn_check(hit):
    comp = (rand.randint(1, 100) + rand.randint(1, 100)) // 2
    if hit >= comp:
        return True
    else:
        return False
    
def print_2darray(a):
    w, h = (len(a[0]), len(a))
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
            if a[i][j] < 10:
                print("0" + str(a[i][j]), end=' ')
            else:
                print(a[i][j], end=' ')
        print('|')
    # print bottom border
    print('-', end=' ')
    for i in range(0, w):
        print('--', end=' ')
    print('-')

# sets tiles in an array
def gen_map(map):
    # for each row, assign 1 to random cells in the row
    for row in map:
        for i in range(len(row)):
            if rand.randint(0,3) == 3:
                row[i] = 1
    
    
    return map

def main():
    rows, cols = (9, 9)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    print_2darray(arr)
    os.system('cls')
    arr = gen_map(arr)
    print_2darray(arr)
    
    #print("console cleared")

if __name__ == "__main__":
    main()