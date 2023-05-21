def main():
    symbol = input()  # start boar with moves: X nand O
    print_board(symbol)


def print_board(setup: str):
    s_setup =list()
    for s in setup:
        s_setup.append(s)

    board = list()
    board.append(s_setup[:3])
    board.append(s_setup[3:6])
    board.append(s_setup[6:10])

    print("--------")
    for i in range(len(board)):
        print("|", end=" ")
        for pos in board[i]:
            print(pos, "", end="")
        print("|")
    print("--------")



if __name__ == '__main__':
    main()
