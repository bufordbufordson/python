# test_weird_numbers.py

import unittest
from weird_number_finder import is_weird


class TestWeirdNumbers(unittest.TestCase):
    def test_initial_weird_numbers(self):
        expected_weird_numbers = [
            70, 836, 4030, 5830, 7192, 7912, 9272, 10430, 10570, 10792, 10990, 11410, 11690, 12110, 12530, 12670, 13370, 13510, 13790, 13930, 14770
        ]
        actual_weird_numbers = []
        candidate = 2
        while len(actual_weird_numbers) < 21:
            if is_weird(candidate):
                actual_weird_numbers.append(candidate)
            candidate += 1
        self.assertEqual(actual_weird_numbers, expected_weird_numbers)

if __name__ == "__main__":
    unittest.main()