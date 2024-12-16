import unittest

from ..Sum_function import sum_func
class TestSumFunction(unittest.TestCase):
    """ Test the Mystery_1 function """
    def test_0(self):
        """Should test the sum of 2 positive integers"""
        self.assertEqual(sum_func(4,6),10)
    def test_1(self):
        """Should test sum of a positive and negative integer"""
        self.assertEqual(sum_func(-10,7),-3)
    def test_2(self):
        """Should test sum of 2 negative integers"""
        self.assertEqual(sum_func(-10,-10),-20)
    def test_3(self):
        """"Should test when a string is input and an error is received"""
        with self.assertRaises(AssertionError):
            sum_func(4, "a")
