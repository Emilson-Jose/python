# made with Python 3.11.5

import random as rand
import subprocess as subp
import os
import pe_map


def hit_calc(a_spd, a_hit, d_avd):
    result = 0
    return result

def rn_check(hit):
    comp = (rand.randint(1, 100) + rand.randint(1, 100)) // 2
    if hit >= comp:
        return True
    else:
        return False

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
    print('===================================================')
    #os.system('cls')
    arr = gen_map(arr)
    #print_2darray(arr)
    pe_map.load_map(arr)
    pe_map.print_map()
    print('===================================================')
    arr = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
    pe_map.load_map(arr)
    pe_map.print_map()
    #print("console cleared")

if __name__ == "__main__":
    main()