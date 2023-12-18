import random as rand

global BOARD; BOARD = [     # -----------
    [' ', ' ', ' '],        # 3 [X][O][O]  Current player: X
    [' ', ' ', ' '],        # 2 [ ][X][ ]  
    [' ', ' ', ' '],        # 1 [ ][ ][ ]
]                           #    A  B  C
                            # -----------
global CUR_PLY; CUR_PLY = 'X'

# check if a move has won the game
# in: current player, last move, BOARD
# out: True if 3-in-a-row has occured
#      False if move did not win
#
#   - run every turn after P1 moves 3 times
#   - check only relevant spaces (if the last move 
#     was bottom right, don't check middle-left)
def win_check():
    return True

# place a player's symbol in the desired square
# in: current player, {user input}
# out (valid pos): update BOARD
# out (invalid pos): prompt user for valid pos
def place_symbol(pos_xy):
    global BOARD; global CUR_PLY
    if pos_xy == -1:
        return True
    pos_y = pos_xy[0]; pos_x = pos_xy[1]
    if BOARD[pos_y][pos_x] == ' ':
        BOARD[pos_y][pos_x] = CUR_PLY
        return False
    else:
        print("invalid position: non-empty")
        return True

# convert user input into coordinates
# in: String user input
# out (valid coord): list [row, col]
# out (invalid coord): print error message,
#                      early escape code for place_symbol
def resolveInput(input):
    coord = set(input)
    if len(coord) != 2:
        print("invalid coordinate: not a letter-digit pair")
        return -1
    
    # check digit component
    if '1' in coord:
        out_pos = [2]
    elif '2' in coord:
        out_pos = [1]
    elif '3' in coord:
        out_pos = [0]
    else:
        print("invalid coordinate: missing valid digit")
        return -1
    
    # check letter component
    if 'A' in coord:
        out_pos.append(0)
    elif 'B' in coord:
        out_pos.append(1)
    elif 'C' in coord:
        out_pos.append(2)
    else:
        print("invalid coordinate: missing valid letter")
        return -1
    return out_pos

# print the game board, current player
def print_game():
    global BOARD; global CUR_PLY
    print("-----------")
    firstRow = True
    row_c = 3           # row numbering var
    for row in BOARD:
        print(str(row_c), end=' ')
        spot_c = 1      # spot counting var
        for spot in row:
            print("[", end='')
            print(spot, end='')
            if spot_c != len(row):  # print w/o line jump until last spot
                print("]", end='')
            spot_c += 1
        if row_c == 3:  # print only after first row
            print("]  Current player:", CUR_PLY)
        else:
            print("]")  # close last spot
        row_c -= 1
    print("   A  B  C")
    print("-----------")

def main():
    print("\n+----- Tic Tac Toe -----+")
    print("+- Three in a row wins -+\n")
    print_game()
    waitMove = True
    while(waitMove):
        user_in = input("Choose a position!: ")
        waitMove = place_symbol(resolveInput(str(user_in).upper()))
    print_game()

if __name__ == "__main__":
    main()