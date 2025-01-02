"""
Created on 02 01 25
"""
import unittest

# --- imports & test class before documenting and testing ---

# from ..constructive_list import consecutive_list

# class TestConstructive_list(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..constructive_list import consecutive_list

class TestConstructiveList(unittest.TestCase):
    """ To test the constructive_list function """

    def test_minimal_input(self):
        """To test for a = 0"""
        actual = consecutive_list(0,0)
        expected = []
        self.assertEqual(actual, expected)
