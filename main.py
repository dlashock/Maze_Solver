from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(1200, 1200)
    num_rows = 10
    num_cols = 12

    maze = Maze(2, 2, num_rows, num_cols, 100, 100, win)


    win.wait_for_close()


main()