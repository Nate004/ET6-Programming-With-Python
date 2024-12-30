"""
test_sort_func.py

This module provides a test for the sort_func function 
to sort a list of integers in ascending order.
"""

import unittest

from ..sort_func import sort_func

class TestMystery5(unittest.TestCase):
    """ This tests for various inputs and outputs """
    def test_minimal_input(self):
        """Test for empty list"""
        self.assertEqual(sort_func([], []), [])

    def test_minimal_input_none(self):
        """Test for empty list and a none"""
        self.assertEqual(sort_func([], None), [])

    def test_only_integers(self):
        """Test with positive integers"""
        self.assertEqual(sort_func([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_list_of_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(sort_func([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]), [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1])
    
    def test_mixed_integers_and_floats(self):
        """Test with a list of mixed integers and floating-point numbers"""
        self.assertEqual(sort_func([3, 1.5, 4.2, 1, 5.5, 9.1, 2, 6.3, 5, 3.3, 5.5]), [1, 1.5, 2, 3, 3.3, 4.2, 5, 5.5, 5.5, 6.3, 9.1])
    
    def test_assert_error_non_integers(self):
        """Test for AssertionError with non-integer inputs"""
        with self.assertRaises(AssertionError):
            sort_func("string", None)
