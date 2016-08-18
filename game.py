# Arda Mavi - ardamavi.com
# Artificial Intelligence Tic Tac Toe

# Imports :
from subprocess import call
from random import randint

# Variables :
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = [board, [], []]
win = "Yet_None"
exit_game = False
order = "O"

# Functions :
def clear_screan():
    call(["clear"])

def print_board(this_board = board):
    print("\n  "+ str(this_board[0]), "|", str(this_board[1]), "|", str(this_board[2]))
    print("  - | - | -")
    print("  "+ str(this_board[3]), "|", str(this_board[4]), "|", str(this_board[5]))
    print("  - | - | -")
    print("  "+ str(this_board[6]), "|", str(this_board[7]), "|", str(this_board[8]), "\n")

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

    return "Yet_None"

def is_finish(this_board):
    if who_win(this_board) == "Yet_None":
        for i in range(9):
            if this_board[i] != "X" and this_board[i] != "O":
                return False
        return True
    else:
        return True

def create_children(board, turn):
    if is_finish(board):
        return []
    tree = []
    for i in range(0,9):
        board_copy = list(board)
        if board_copy[i] == "X" or board_copy[i] == "O":
            continue
        board_copy[i] = turn
        tree.append(board_copy)
    return list(tree)

def bf_creator(root, turn):
    tree = []
    queue = [(tree, root, turn)]
    tree.append(root)
    while queue != []:
        elem = queue[0]
        queue.remove(elem)
        children = create_children(elem[1], elem[2])
        tmp_turn = "O" if elem[2] == "X" else "X"
        for child in children:
            elem[0].append([child])
            queue.append((elem[0][-1], child, tmp_turn))
    return tree

def leaves(tree):
    last_children = []
    queue = [tree]
    while queue != []:
        elem = queue[0]
        queue.remove(elem)
        if len(elem) == 1:
            last_children.append(elem[0])
        elif len(elem) > 1:
            for child in elem[1:]:
                queue.append(child)
    return last_children

def where_ai(this_tree):
    probabilities = []

    for i in this_tree[1:]:
        leaves = leaves(i)
        count = 0
        for leave in leaves:
            if who_win(leave) == "X":
                count += 1
            elif who_win(leave) == "O":
                count -= 1
        probabilities.append([count/len(leaves), i[0]])

    bigger = [-10000, []]
    for i in probabilities:
        if i[0] > bigger[0]:
            bigger = i

    return bigger[1]

def play_game(inpt):
    global board
    board[inpt-1] = "X"
    if who_win(board) == "Yet_None":
        play_len = 0
        for i in range(0,9):
            if board[i] == "X" or board[i] == "O":
                play_len += 1
        if play_len <= 1:
            bf_creator(board, "O")
        else:
            for i in tree[1:]:
                if i[0] == board:
                    tree = i
                    break
        board = where_ai(tree)

# Main :
clear_screan()
print("Artificial Intelligence Tic Tac Toe\nArda Mavi - ardamavi.com\nExit Game: 0")
win = "Yet_None"
order = "O"

while win == "Yet_None":
    print_board()

    while True:
        inpt = input("X's turn: ")
        if int(inpt) == 0:
            win = "None"
            break
        elif is_free(board, int(inpt)):
            play_game(int(inpt))
            win = who_win(board)
            break
        else:
            clear_screan()
            print("Try Again !")
            print_board()
    clear_screan()
clear_screan()
print_board()
print("Win: " + win)
print("Arda Mavi - ardamavi.com\nThe End !\n")
