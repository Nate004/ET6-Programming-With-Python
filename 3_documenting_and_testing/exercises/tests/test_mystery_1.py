import unittest

from ..mystery_1 import mystery_1
class TestMystery1(unittest.TestCase):
    """ Test the Mystery_1 function """
    def test_0(self):
        """It should evaluate 0 to []"""
        self.assertEqual(mystery_1(0))
