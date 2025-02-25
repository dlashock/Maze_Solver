from point import Point
from line import Line
from window import Window

class Cell:
    def __init__(self, x1, x2, y1, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self, fill_color):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            tl_bl = Line(top_left, bottom_left)
            self._win.draw_line(tl_bl, fill_color)
        if self.has_right_wall:
            tr_br = Line(top_right, bottom_right)
            self._win.draw_line(tr_br, fill_color)
        if self.has_top_wall:
            tl_tr = Line(top_left, top_right)
            self._win.draw_line(tl_tr, fill_color)
        if self.has_bottom_wall:
            bl_br = Line(bottom_left, bottom_right)
            self._win.draw_line(bl_br, fill_color)

    def draw_move(self, to_cell, undo=False):
        '''if undo:
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
        self._win.draw_line(line, fill_color)'''
    
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)