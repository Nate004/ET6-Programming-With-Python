"""
Created on 13 01 25

@author: Taiwo Babatunde

"""

# import unittest

# --- imports & test class before documenting and testing ---

# from ..mystery_7 import mystery_7

# class TestMystery7(unittest.TestCase):

# --- imports & test class after documenting and testing ---

import unittest

from ..list_filter import list_filter

class test_list_filter(unittest.TestCase):
    """ This should test the list_filter function """

    def test_0(self):
        """It should evaluate (["apple", "banana", "cherry"], "a") to ['apple', 'banana']"""
        actual = list_filter(["apple", "banana", "cherry"], "a")  
        expected = ['apple', 'banana']  
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate (["dog", "cat", "mouse"], "o") to ['dog', 'mouse']"""
        actual = list_filter(["dog", "cat", "mouse"], "o")
        expected = ['dog', 'mouse']
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate (["hello", "world"], "z") to []"""
        actual = list_filter(["hello", "world"], "z")
        expected = []
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should evaluate test successfully"""
        actual = list_filter(["test", "testing", "tested"], "test")
        expected = ['test', 'testing', 'tested']
        self.assertEqual(actual, expected)

    def test_not_a_list_of_strings(self):
        """It should raise an assertion error if the first argument is not a list of strings"""
        with self.assertRaises(AssertionError):
            list_filter("not a list", "a")
        with self.assertRaises(AssertionError):
            list_filter([1, 2, 3], "a")

    def test_not_a_string(self):
        """It should raise an assertion error if the second argument is not a string"""
        with self.assertRaises(AssertionError):
            list_filter(["apple", "banana"], 1)
