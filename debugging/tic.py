#!/usr/bin/python3
"""
Tic-Tac-Toe Game Implementation.

This script provides a simple implementation of the classic Tic-Tac-Toe game.
Players alternate between "X" and "O" to mark cells on a 3x3 board.
The game continues until a player wins or the board is full and the game
ends in a draw.

Functions
---------
print_board(board)
    Displays the current state of the game board.
check_winner(board)
    Checks if there is a winner on the current board.
check_draw(board)
    Checks if the game is a draw (i.e., the board is full and no winner).
tic_tac_toe()
    Runs the main game loop for Tic-Tac-Toe.
"""


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
        print("-" * (len(row) * 4 - 1))


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
    size = len(board)

    # Check rows and columns
    for i in range(size):
        if all(board[i][j] == board[i][0] and board[i][0] != " " for j in range(size)):
            return True
        if all(board[j][i] == board[0][i] and board[0][i] != " " for j in range(size)):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[0][0] != " " for i in range(size)):
        return True
    if all(
        board[i][size - 1 - i] == board[0][size -
                                           1] and board[0][size - 1] != " "
        for i in range(size)
    ):
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
    return all(cell != " " for row in board for cell in row) and not check_winner(board)


def tic_tac_toe():
    """
    Run the Tic-Tac-Toe game.

    This function initializes the game board and alternates between players "X"
    and "O". Players are prompted to enter their move until there is a winner
    or the game ends in a draw.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(
                input(f"Enter column (0, 1, or 2) for player {player}: "))
            if not (0 <= row < 3 and 0 <= col < 3):
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
