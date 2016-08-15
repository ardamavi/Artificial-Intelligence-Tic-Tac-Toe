# Arda Mavi - ardamavi.com
# Artificial Intelligence Tic Tac Toe

# Imports :
from subprocess import call
from random import randint

# Variables :
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = "Yet_None"
exit_game = False
order = "O"

# Functions :
def clear_screan():
    call(["clear"])

def print_board():
    print("\n  "+ str(board[0]), "|", str(board[1]), "|", str(board[2]))
    print("  - | - | -")
    print("  "+ str(board[3]), "|", str(board[4]), "|", str(board[5]))
    print("  - | - | -")
    print("  "+ str(board[6]), "|", str(board[7]), "|", str(board[8]), "\n")

def start_settings():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win = "Yet_None"
    order = "O"

def is_free(this_board, inpt):
    if this_board[inpt-1] == "X" or this_board[inpt-1] == "O":
        return False
    else:
        if int(inpt) > 0 and int(inpt) <= 9:
            return True
        else:
            return False

def who_win(this_board):
    # Horizontal
    for i in range(0,7,3):
        if (this_board[i] == 'X' and this_board[i+1] == 'X' and this_board[i+2] == 'X') or (this_board[i] == 'O' and this_board[i+1] == 'O' and this_board[i+2] == 'O'):
            return board[i+1]

    # Vertical
    for i in range(3):
        if (this_board[i] == 'X' and this_board[i+3] == 'X' and this_board[i+6] == 'X') or (this_board[i] == 'O' and this_board[i+3] == 'O' and this_board[i+6] == 'O'):
            return board[i+3]

    # Cross
    if (this_board[0] == 'X' and this_board[4] == 'X' and this_board[8] == 'X') or (this_board[0] == 'O' and this_board[4] == 'O' and this_board[8] == 'O'):
        return board[4]

    if (this_board[2] == 'X' and this_board[4] == 'X' and this_board[6] == 'X') or (this_board[2] == 'O' and this_board[4] == 'O' and this_board[6] == 'O'):
        return board[4]

    if is_finish():
        return "None"

    return "Yet_None"

def is_finish(this_board):
    for i in range(9):
        if this_board[i] != "X" and this_board[i] != "O":
            return False
    if who_win(this_board) != "Yet_None":
        return True
    else:
        return True

def where_ai():
    # ai's Turn

def ai_play():
    board[where_ai()+1] = "O"

def play_game(inpt):
        board[inpt-1] = "X"
        if who_win(board) == "Yet_None":
            ai_play()

# Main :
clear_screan()
print("Artificial Intelligence Tic Tac Toe\nArda Mavi - ardamavi.com\nExit Game: 0")
start_settings()

while win == "Yet_None":
    clear_screan()
    print_board()

    while True:
        inpt = input("X's turn: ")
        if int(inpt) == 0:
            win = "None"
            break
        elif is_free(this_board, int(inpt)):
            play_game(int(inpt))
            win = who_win(board)
            break
        else:
            clear_screan()
            print("Try Again !")
            print_board()

clear_screan()
print_board()
print("Win: " + win)
print("Arda Mavi - ardamavi.com\nThe End !\n")
