from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(1210, 1010)
    num_rows = 10
    num_cols = 12

    maze = Maze(5, 5, num_rows, num_cols, 100, 100, win)
    maze.solve()

    win.wait_for_close()


main()