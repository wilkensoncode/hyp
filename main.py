def main():
    board = [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]]  # 3X3 tic-tac-to board
    print_board(board)

def print_board(board: list):
    for i in range(len(board)):
        for pos in board[i]:
            print(pos, " ", end="")
        print()


if __name__ == '__main__':
    main()
