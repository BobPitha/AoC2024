import unittest
from Day04.day04_main import solve_part_1, solve_part_2, read_input, is_x_mas

class TestSolutions(unittest.TestCase):
    def test_read_input(self):
        lines = read_input("Day04/example.txt")
        self.assertEqual(len(lines), 10)

    def test_part1(self):
        lines = read_input("Day04/example.txt")
        self.assertEqual(solve_part_1(lines), 18)

    def test_part2(self):
        lines = read_input("Day04/example.txt")
        self.assertEqual(solve_part_2(lines), 9)
    
    def test_is_x_mas_valid_expect_true(self):
        lines=["MQM", "ZAX", "SSS"]
        self.assertTrue(is_x_mas(lines, 1, 1))
    
    def test_is_x_mas_invalid_expect_false(self):
        lines=["MQS", "ZAX", "SSS"]
        self.assertFalse(is_x_mas(lines, 1, 1))

if __name__ == "__main__":
    unittest.main()