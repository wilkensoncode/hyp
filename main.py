def main():
    board = process_input('XOXOOXXXO')
    print_board(board)

    if is_full(board) and not is_winner(board):
        print("Draw")
    elif is_winner(board) and is_winner(board):
        print(f"{is_winner(board)} wins")
    elif not is_full(board) and not is_winner(board) and not is_impossible(board):
        print("Game not finished")
    elif is_impossible(board) or is_impossible(board) and is_winner(board):
        print("Impossible")


def is_full(board: list):
    for row in board:
        if "_" in row:
            return False
    return True


def is_impossible(board: list):
    count_x = sum(row.count("X") for row in board)
    count_O = sum(row.count("O") for row in board)
    diff = abs(count_O - count_x)
    if diff >= 2:
        return True

    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return True

    return False


def incomplete_game(board: list):
    count_x = sum(row.count("X") for row in board)
    count_O = sum(row.count("O") for row in board)
    diff = abs(count_O - count_x)

    wins_x = is_winner(board) == "X"
    wins_O = is_winner(board) == "O"
    # print(wins_O, wins_x)

    if wins_x == wins_O or diff <= 1:
        return True
    return False


def is_winner(board: list):
    winners = list()
    for row in board:  # check row winner
        if row[0] == row[1] == row[2] and row[0] != "_":
            winners.append(row[0])

    for col in range(len(board)):  # check columns winner
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            winners.append(board[0][col])

    # check diagonal winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        winners.append((board[0][0]))
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        winners.append(board[0][2])

    winner = len(winners)

    if winner == 1:
        return winners[0]
    elif winner > 1:
        return False  # impossible game
    return False


def print_board(board: list):
    print("---------")
    for i in range(len(board)):
        print("|", end=" ")
        for pos in board[i]:
            print(pos, "", end="")
        print("|")
    print("---------")


def process_input(string: str):  # @param str len must be 9 and choices are X O _
    board_setup = list()
    for s in string:
        board_setup.append(s)

    board = list()

    board.append(board_setup[:3])
    board.append(board_setup[3:6])
    board.append(board_setup[6:10])
    return board


if __name__ == '__main__':
    main()
