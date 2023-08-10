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

def main():
    rows, cols = (15, 15)
    print("================")
    # method 2 2nd approach
    arr = [[0 for i in range(cols)] for j in range(rows)]
    #for row in arr:
    #    print(row)
    print_2darray(arr)
    #os.system('cls')
    #print("console cleared")

if __name__ == "__main__":
    main()