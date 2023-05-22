def main():
    instructions = """
        Game start with empty board
        X is the first player
        to start playing enter a coordinate eg. 4 1
        1 1 being the left upper corner of the board
        3 3 being the bottom right corner of the board 
        """
    print(instructions)
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    play_game(board)


def state(board):
    if is_winner(board):
        print(f"{is_winner(board)} wins")
        pass
    elif is_full(board):
        print("Draw")


def play_game(board: list):
    cell_taken = "This cell is occupied! Choose another one!"
    wrong_input = "You should enter numbers!"
    wrong_position = "Coordinates should be from 1 to 3!"

    current_player = 'X'

    while True:
        pos_row, pos_col = input().split()
        if not pos_col.isnumeric() and not pos_row.isnumeric():
            print(wrong_input)
        else:
            pos_row = int(pos_row)
            pos_col = int(pos_col)

            if pos_row > 3 or pos_col > 3:
                print(wrong_position)
            elif board[pos_row - 1][pos_col - 1] == " ":
                board[pos_row - 1][pos_col - 1] = current_player
                print_board(board)
                if is_winner(board):
                    state(board)
                    break
                elif is_full(board):
                    state(board)
                    break

            else:
                print(cell_taken)
            current_player = 'O' if current_player == 'X' else 'X'  # switch player


def is_full(board: list):
    for row in board:
        if " " in row:
            return False
    return True


def is_winner(board: list):
    winners = list()
    for row in board:  # check row winner
        if row[0] == row[1] == row[2] and row[0] != " ":
            winners.append(row[0])

    for col in range(len(board)):  # check columns winner
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            winners.append(board[0][col])

    # check diagonal winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        winners.append((board[0][0]))
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        winners.append(board[0][2])

    winner = len(winners)
    if winner == 1:
        return winners[0]
    elif winner > 1:
        return False  # impossible game
    return False  # draw


def print_board(board: list):
    print("---------")
    for i in range(len(board)):
        print("|", end=" ")
        for pos in board[i]:
            print(pos, "", end="")
        print("|")
    print("---------")


if __name__ == '__main__':
    main()
