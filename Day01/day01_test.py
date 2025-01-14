import unittest
from Day01.day01_main import solve_part_1, solve_part_2, read_input

class TestSolutions(unittest.TestCase):
    def test_part1(self):
        test_data_1, test_data_2 = read_input("Day01/example1.txt")
        self.assertEqual(solve_part_1(test_data_1, test_data_2), 11)

    def test_part2(self):
        test_data_1, test_data_2 = read_input("Day01/example1.txt")
        self.assertEqual(solve_part_2(test_data_1, test_data_2), 31)

if __name__ == "__main__":
    unittest.main()