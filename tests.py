import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_x_y(self):
        y_val = 50
        x_val = 10
        m1 = Maze(x_val, y_val, 10, 12, 10, 10)

        self.assertEqual(
            m1.x1,
            x_val,
        )
        self.assertEqual(
            m1.y1,
            y_val,
        )

    def test_maze_cell_size(self):
        cell_size_x = 50
        cell_size_y = 25
        m1 = Maze(10, 10, 10, 12, cell_size_x, cell_size_y)

        self.assertEqual(
            m1.cell_size_x,
            cell_size_x,
        )
        self.assertEqual(
            m1.cell_size_y,
            cell_size_y,
        )

if __name__ == "__main__":
    unittest.main()