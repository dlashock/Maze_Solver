from point import Point
from line import Line
from window import Window

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, top_left_x, bottom_right_x, top_left_y, bottom_right_y, fill_color):
        self._x1 = top_left_x
        self._x2 = bottom_right_x
        self._y1 = top_left_y
        self._y2 = bottom_right_y

        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        
        tl_bl = Line(top_left, bottom_left)
        tr_br = Line(top_right, bottom_right)
        tl_tr = Line(top_left, top_right)
        bl_br = Line(bottom_left, bottom_right)
                
        if self.has_left_wall:    
            self._win.draw_line(tl_bl, fill_color)
        elif not self.has_left_wall:
            self._win.draw_line(tl_bl, "white")

        if self.has_right_wall:
            self._win.draw_line(tr_br, fill_color)
        elif not self.has_right_wall:
            self._win.draw_line(tr_br, "white")

        if self.has_top_wall:
            self._win.draw_line(tl_tr, fill_color)
        elif not self.has_top_wall:
            self._win.draw_line(tl_tr, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bl_br, fill_color)
        elif not self.has_bottom_wall:
            self._win.draw_line(bl_br, "white")

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        
        cell_1_x = (self._x1 + self._x2) // 2
        cell_1_y = (self._y1 + self._y2) // 2
        cell_1_point = Point(cell_1_x, cell_1_y)

        cell_2_x = (to_cell._x1 + to_cell._x2) // 2
        cell_2_y = (to_cell._y1 + to_cell._y2) // 2
        cell_2_point = Point(cell_2_x, cell_2_y)

        line = Line(cell_1_point, cell_2_point)
        self._win.draw_line(line, fill_color)