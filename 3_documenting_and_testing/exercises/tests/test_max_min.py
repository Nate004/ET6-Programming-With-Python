import unittest

from ..Max_Min_Function import max_min

class TestMystery3(unittest.TestCase):
    """To test for minimum/maximum inputs"""
    def test_equal_input(self):
        """Test when the inputs are equal integers i.e. a=b"""
        self.assertEqual(max_min(10, 10), 20)
    def test_minimum_input(self):
        """Test for minimum value between a & b"""
        self.assertEqual(max_min(4, 6), 4)
    def test_maximum_input(self):
        """Test for maximum value between a & b"""
        self.assertEqual(max_min(10, 9), 9)
    def test_negative_input(self):
        """Test for negative integers value between a & b"""
        self.assertEqual(max_min(-10, -9), -10)
    def test_non_integer_input_error(self):
        """This should raise an AssertionError for non-integers or strings"""
        with self.assertRaises(AssertionError):
            max_min("a", 5)
