#!/usr/bin/python3

import os
import random


def clear_screen():
    """Clear the screen."""
    os.system("cls" if os.name == "nt" else "clear")


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        """Initialize variables of the class."""
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[" " for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_cells = width * height
        self.revealed_cells = 0

    def print_board(self, reveal=False):
        """Display the map."""
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
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (
                    (dx != 0 or dy != 0)
                    and 0 <= nx < self.width
                    and 0 <= ny < self.height
                ):
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
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
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= self.width and 0 <= y < self.height):
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
