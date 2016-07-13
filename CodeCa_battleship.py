board = []

for i in range(5):
    board.append(['O'] * 5)
print board


def print_board(board):
    for i in range(len(board)):
        print board[i]

print print_board(board)