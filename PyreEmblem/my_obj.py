# made with Python 3.11.5

import random as rand
import subprocess as subp
import os
import pe_map

global CLASS_BASES; CLASS_BASES = [
    [20, 5, 1, 1, 0, 1, 8],     # default unit bases
    [15, 3, 8, 6, 0, 4, 2],     # Sword Fighter
    [18, 4, 6, 6, 0, 3, 3],     # Lance Fighter
    [],     # Axe Fighter
    [],     # Bow Fighter
    [],     # Cavalry
    [],     # Knight
    [],     # Mage
    [],     # Trainee
    [],     # Pegasus Rider
]

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
        treeChance = 4
        for i in range(len(row)):
            if map.index(row)-1 > 0:
                if map[map.index(row)-1][i] == 1:
                    treeChance = 2
            if i-1 > 0:
                if row[i-1] == 1:
                    treeChance = 2
            if map.index(row)+1 < len(map):
                if map[map.index(row)+1][i] == 1:
                    treeChance = 2
            if i+1 < len(row):
                if row[i+1] == 1:
                    treeChance = 2
            if rand.randint(0,treeChance) == 0:
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
    # FE8 Chapter 5, "The Empire's Reach" map
    arr = [[0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0],
           [0, 7, 3, 7, 7, 3, 7, 7, 7, 7, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 0],
           [1, 0, 7, 0, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 0],
           [0, 0, 7, 0, 7, 3, 7, 7, 7, 0, 0, 7, 3, 7, 0],
           [0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
           [0, 1, 7, 0, 0, 7, 7, 7, 0, 0, 0, 7, 7, 7, 7],
           [0, 0, 7, 0, 0, 7, 3, 7, 0, 0, 0, 7, 3, 7, 7],
           [0, 0, 7, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 7, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 7, 7],
           [7, 0, 7, 0, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 7],
           [7, 0, 7, 0, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
           [7, 7, 7, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 0],
           [7, 7, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 0],
           [7, 7, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 3, 7, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    pe_map.load_map(arr)
    pe_map.print_map()
    #os.system('cls')
    #print("console cleared")

    #player_units = []      # list of Units controlled by player
    #enemy_units = []       # list of Units controlled by AI

if __name__ == "__main__":
    main()