import os
import time

def getFrame(frm_no):
    if frm_no == 0:
        return "      ,\n     /\\\n    /  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 1:
        return "      ,\n     /\\\n .  /  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 2:
        return "      ,\n     /\\\n .. /  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 3:
        return "      ,\n     /\\\n .../  \\\n @_/    \\\n\(_      \\\n X L    ~~\\~~~~\n"
    if frm_no == 4:
        return "      ,\n     /\\\n  ! /  \\\n @_/    \\\n\(_      \\\n X L    ~w\\w~~~\n"

#      ,       
#     /\       
#    /  \      
# @_/    \     
#\(_      \    
# X L    ~~\~~~

def main():
    c = 0
    while c < 5:
        os.system('cls')
        print(getFrame(c))
        c += 1
        time.sleep(.5)

if __name__ == "__main__":
    main()