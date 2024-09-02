#!/usr/bin/python3

import os
import random


def clear_screen():
    """Clear the screen."""
    os.system("cls" if os.name == "nt" else "clear")


class Minesweeper:
    """
    A simple Minesweeper game implementation.

    Attributes
    ----------
    width : int
        The width of the game field.
    height : int
        The height of the game field.
    mines : set
        A set of mine positions.
    field : list
        The game field with cells represented by spaces.
    revealed : list
        A boolean matrix indicating which cells have been revealed.
    total_cells : int
        The total number of cells in the game field.
    revealed_cells : int
        The number of cells that have been revealed.
    """

    def __init__(self, width=10, height=10, mines=10):
        """
        Initialize the Minesweeper game.

        Parameters
        ----------
        width : int, optional
            The width of the game field (default is 10).
        height : int, optional
            The height of the game field (default is 10).
        mines : int, optional
            The number of mines in the game field (default is 10).
        """
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[" " for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_cells = width * height
        self.revealed_cells = 0

    def print_board(self, reveal=False):
        """
        Display the game field.

        Parameters
        ----------
        reveal : bool, optional
            If True, reveal all cells (default is False).
        """
        clear_screen()
        print("  " + " ".join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=" ")
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print("*", end=" ")
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else " ", end=" ")
                else:
                    print(".", end=" ")
            print()

    def count_mines_nearby(self, x, y):
        """
        Count the number of mines in adjacent cells.

        Parameters
        ----------
        x : int
            The x-coordinate of the cell.
        y : int
            The y-coordinate of the cell.

        Returns
        -------
        int
            The number of adjacent mines.
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Reveal the cell at the given coordinates.

        Parameters
        ----------
        x : int
            The x-coordinate of the cell.
        y : int
            The y-coordinate of the cell.

        Returns
        -------
        bool
            True if the cell was revealed successfully, False if it was a mine.
        """
        if (y * self.width + x) in self.mines:
            return False
        if not self.revealed[y][x]:
            self.revealed[y][x] = True
            self.revealed_cells += 1
            if self.count_mines_nearby(x, y) == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < self.width
                            and 0 <= ny < self.height
                            and not self.revealed[ny][nx]
                        ):
                            self.reveal(nx, ny)
        return True

    def play(self):
        """Main game loop to play Minesweeper."""
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Please enter valid coordinates.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.revealed_cells == self.total_cells - len(self.mines):
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
