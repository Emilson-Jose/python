# buffering inputs can be abused

import os
import time
import random

def getFrame(frm_no):
    if frm_no == 0:
        return "      ,      ~Fishing Minigame~\n     /       Press Enter to cast\n    /  \n @_/    \n\(_      \n X L    ~~~~~~~"
    if frm_no == 1:
        return "      ,\n     /\\\n    /  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 2:
        return "      ,\n     /\\\n .  /  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 3:
        return "      ,\n     /\\\n .. /  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 4:
        return "      ,\n     /\\\n .../  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 5:
        return "      ,\n     /\\\n  ! /  \\\n @_/    \\\n\(_      \\\n X L    ~w\\w~~~\n"
    if frm_no == 6:
        return "      ,\n     /\\\n    /  \\\n @_/    \\\n\(_      \\\n X L    ~w\\w~~~\n"

#      ,       
#     /\       
#    /  \      
# @_/    \     
#\(_      \    
# X L    ~~\~~~

def main():
    c = 0
    fishAttempts = []
    frameOdds = [1, 5, 9, 37]
    os.system('cls')
    print(getFrame(c))
    print("press Enter when you see ! above the fisher")
    input()
    c += 1
    while c < 5:
        os.system('cls')
        print(getFrame(c))
        if (random.randint(1, 100) <= frameOdds[c-1]):
            time.sleep(0.4)
            os.system('cls')
            print(getFrame(5))
            reaction = time.time()
            input()
            reaction = time.time() - reaction
            print("reaction time:", reaction)
            fishAttempts.append(reaction)
            if reaction < 0.8:
                print("You caught one!")
                print("Input \"Q\" to exit or press Enter to go again")
                if str(input()).upper() == 'Q':
                    break
                else:
                    c = 1
                    time.sleep(.35)
            else:
                print("It got away...")
                c = 1
                time.sleep(1.86)
        else:
            c %= 4
            c += 1
            time.sleep(1.4)
    print("Session stats")
    fishAttempts.sort()
    fishMiss = []
    for x in fishAttempts:
        if x > 0.8:
            fishMiss.append(fishAttempts.pop())
    print("Fish caught:", len(fishAttempts))
    print("Fish misses:", len(fishMiss))
    print("")

if __name__ == "__main__":
    main()