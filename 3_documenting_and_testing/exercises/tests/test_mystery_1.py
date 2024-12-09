import unittest

from ..mystery_1 import sort_bubble
class TestMystery1(unittest.TestCase):
    """ Test the Mystery_1 function """
    def test_0(self):
        """Should test that the list is sorted and remains unchanged"""
        self.assertEqual(sort_bubble([0,1,3,4,5,6]),[0,1,3,4,5,6])
    def test_1(self):
        """Should test for reversed sorted list"""
        self.assertEqual(sort_bubble([6,5,4,3,2,1,0]),[0,1,2,3,4,5,6])
    def test_2(self):
        """Should sort list in correct ascending order"""
        self.assertEqual(sort_bubble([0,2,1,3,6,5,4]),[0,1,2,3,4,5,6])
