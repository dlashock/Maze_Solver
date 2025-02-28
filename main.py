from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(802, 602)
    num_rows = 10
    num_cols = 12

    maze = Maze(0, 0, num_rows, num_cols, 50, 50, win)
    
    win.wait_for_close()


main()