import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        initial_visited_count = 0
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                if m1._cells[i][j].visited == True:
                    initial_visited_count += 1
        m1._reset_cells_visited()
        final_visited_count = 0
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                if m1._cells[i][j].visited == True:
                    final_visited_count += 1


        
        self.assertEqual(
            final_visited_count,
            0,
        )
        self.assertNotEqual(
            initial_visited_count,
            final_visited_count,
        )

if __name__ == "__main__":
    unittest.main()