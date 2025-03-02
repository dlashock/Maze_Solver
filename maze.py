from cell import Cell
import time
import random

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
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(j, i)

    def _draw_cell(self, j, i):
        if self._win is None:
            return
        x1_pos = self.x1 + (i * self.cell_size_x)
        y1_pos = self.y1 + (j * self.cell_size_y)
        x2_pos = self.x1 + ((i + 1) * self.cell_size_x)
        y2_pos = self.y1 + ((j + 1) * self.cell_size_y)
        self._cells[i][j].draw(x1_pos, x2_pos, y1_pos, y2_pos, "black")
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
            
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[j][i].visited = True
        while(True):
            to_visit = []
            if i > 0 and self._cells[j][i-1].visited == False:
                to_visit.append((j, i-1))
            if j > 0 and self._cells[j-1][i].visited == False:
                to_visit.append((j-1, i))
            if i+1 < self.num_rows and self._cells[j][i+1].visited == False:
                to_visit.append((j, i+1))
            if j+1 < self.num_cols and self._cells[j+1][i].visited == False:
                to_visit.append((j+1, i))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            cell = random.randrange(0, len(to_visit), 1)
            adj_j = to_visit[cell][0]
            adj_i = to_visit[cell][1]
           
            if adj_j > j:
                self._cells[adj_j][adj_i].has_left_wall = False
                self._cells[j][i].has_right_wall = False
            elif adj_j < j:
                self._cells[adj_j][adj_i].has_right_wall = False
                self._cells[j][i].has_left_wall = False
            elif adj_i > i:
                self._cells[adj_j][adj_i].has_top_wall = False
                self._cells[j][i].has_bottom_wall = False
            elif adj_i < i:
                self._cells[adj_j][adj_i].has_bottom_wall = False
                self._cells[j][i].has_top_wall = False
            self._break_walls_r(adj_i, adj_j) 