from cell import Cell
from window import Window
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for x in range(self.num_cols):
            for y in range(self.num_rows):
                self._draw_cell(y, x)

    def _draw_cell(self, y, x):
        if self._win is None:
            return
        x1_pos = self.x1 + (x * self.cell_size_x)
        y1_pos = self.y1 + (y * self.cell_size_y)
        x2_pos = self.x1 + ((x + 1) * self.cell_size_x)
        y2_pos = self.y1 + ((y + 1) * self.cell_size_y)
        self._cells[x][y].draw(x1_pos, x2_pos, y1_pos, y2_pos, "black")
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
