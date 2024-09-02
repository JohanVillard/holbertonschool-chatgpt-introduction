#!/usr/bin/python3


def print_board(board):
    """
    Display the current game board.

    Parameters
    ----------
    board : list of list of str
        A 2D list representing the Tic-Tac-Toe board, where each element is
        either "X", "O", or " " (empty space).
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Check if there's a winner in the current game board.

    Parameters
    ----------
    board : list of list of str
        A 2D list representing the Tic-Tac-Toe board.

    Returns
    -------
    bool
        True if there is a winner, otherwise False.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_draw(board):
    """
    Check if the game is a draw (i.e., board is full and no winner).

    Parameters
    ----------
    board : list of list of str
        A 2D list representing the Tic-Tac-Toe board.

    Returns
    -------
    bool
        True if the board is full and no player has won, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Run the Tic-Tac-Toe game.

    This function initializes the game board and alternates between players "X" and "O".
    Players are prompted to enter their move until there is a winner or the game ends in a draw.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Please enter a number between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")


if __name__ == "__main__":
    tic_tac_toe()
