"""
Created on 02 01 25
"""

import unittest

# --- imports & test class before documenting and testing ---

# from ..consecutive_list import consecutive_list

# class TestConsecutiveList(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..consecutive_list import consecutive_list


class TestConstructiveList(unittest.TestCase):
    """To test the constructive_list function"""

    def test_minimal_input(self):
        """To test for a = 0"""
        actual = consecutive_list(0, 0)
        expected = []
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate (4, 5) to [5, 6, 7, 8]"""
        actual = consecutive_list(4, 5)
        expected = [5, 6, 7, 8]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate (3, 10) to [10, 11, 12]"""
        actual = consecutive_list(3, 10)
        expected = [10, 11, 12]
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should evaluate (5, 0) to [0, 1, 2, 3, 4]"""
        actual = consecutive_list(5, 0)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(actual, expected)

    def test_less_than_0(self):
        """It should raise an assertion error if the first argument is less than 0"""
        with self.assertRaises(AssertionError):
            consecutive_list(-1, 5)

    def test_not_an_integer(self):
        """It should raise an assertion error if the arguments are not integers"""
        with self.assertRaises(AssertionError):
            consecutive_list(1.0, 5)
        with self.assertRaises(AssertionError):
            consecutive_list(4, "5")
