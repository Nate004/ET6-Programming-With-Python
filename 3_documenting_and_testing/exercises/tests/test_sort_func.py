import unittest

from ..sort_func import sort_func

class TestMystery5(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(sort_func([], []), [])

    def test_minimal_input_none(self):
        """"""
        self.assertEqual(sort_func([], None), [])

    def test_minimal_input_default_argument(self):
        """"""
        self.assertEqual(sort_func([]), [])
