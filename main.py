from window import Window
from point import Point
from line import Line

def main():
    p1 = Point(25, 25)
    p2 = Point(50, 50)
    p3 = Point(248, 443)
    p4 = Point(563, 142)
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    fill_color = "black"

    win = Window(800, 600)
    win.draw_line(line1, fill_color)
    win.draw_line(line2, fill_color)
    win.wait_for_close()


main()