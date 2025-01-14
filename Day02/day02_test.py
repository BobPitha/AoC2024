import unittest
from Day02.day02_main import solve_part_1, solve_part_2, read_input, is_safe, is_safe_with_dampener

class TestSolutions(unittest.TestCase):
    def test_part1(self):
        test_data = read_input("Day02/example.txt")
        self.assertEqual(solve_part_1(test_data), 2)

    def test_part2(self):
        test_data = read_input("Day02/example.txt")
        self.assertEqual(solve_part_2(test_data), 4)

    def test_is_safe_with_valid_input_all_increasing_expect_1(self):
        report = [1, 2, 4, 7]
        self.assertEqual(is_safe(report), 1)

    def test_is_safe_with_valid_input_all_decreasing_expect_1(self):
        report = [9, 8, 6, 3]
        self.assertEqual(is_safe(report), 1)

    def test_is_safe_with_invalid_input_not_all_increasing_expect_0(self):
        report = [5, 7, 6, 8, 11]
        self.assertEqual(is_safe(report), 0)

    def test_is_safe_with_invalid_input_not_all_decreasing_expect_0(self):
        report = [19, 18, 20, 17, 15]
        self.assertEqual(is_safe(report), 0)

    def test_is_safe_invalid_input_same_level_expect_0(self):
        report = [25, 27, 27, 29]
        self.assertEqual(is_safe(report), 0)

    def test_is_safe_invalid_input_multiple_errors_expect_0(self):
        report = [36, 40, 39, 32, 33]
        self.assertEqual(is_safe(report), 0)

    def test_is_safe_with_dampener_valid_input_all_increasing_expect_1(self):
        report = [1, 2, 4, 7]
        self.assertEqual(is_safe_with_dampener(report), 1)

    def test_is_safe_with_dampener_valid_input_all_decreasing_expect_1(self):
        report = [9, 8, 6, 3]
        self.assertEqual(is_safe_with_dampener(report), 1)

    def test_is_safe_with_dampener_invalid_input_not_all_increasing_expect_1(self):
        report = [5, 7, 6, 8, 11]
        self.assertEqual(is_safe_with_dampener(report), 1)

    def test_is_safe_with_dampener_invalid_input_not_all_decreasing_expect_1(self):
        report = [19, 18, 20, 17, 15]
        self.assertEqual(is_safe_with_dampener(report), 1)

    def test_is_safe_with_dampener_invalid_input_same_level_expect_1(self):
        report = [25, 27, 27, 29]
        self.assertEqual(is_safe_with_dampener(report), 1)

    def test_is_safe_with_dampener_invalid_input_multiple_errors_expect_0(self):
        report = [36, 40, 39, 32, 33]
        self.assertEqual(is_safe_with_dampener(report), 0)

if __name__ == "__main__":
    unittest.main()