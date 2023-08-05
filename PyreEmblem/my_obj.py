# made with Python 3.10.11

import random as rand

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

def main():
    rows, cols = (5, 5)
    print("================")
    # method 2 2nd approach
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for row in arr:
        print(row)

if __name__ == "__main__":
    main()