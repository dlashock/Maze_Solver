from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(25, 50, 25, 50, win)
    c2 = Cell(225, 250, 225, 250, win)
    fill_color = "black"

    c1.draw(fill_color)
    c2.draw(fill_color) 
    
    win.wait_for_close()


main()