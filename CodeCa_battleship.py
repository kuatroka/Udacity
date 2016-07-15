from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print " ".join(row)


# Add your code below!
def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)


guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Column: "))

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"


