#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_One(self):
        """first test
        """
        max = max_integer([4, 3, 5, 1])
        self.assertEqual(max, 5)
        max = max_integer([0, -1, -10, -50])
        self.assertEqual(max, 0)
        max = max_integer([1])
        self.assertEqual(max, 1)
        max = max_integer([1, 2, 5])
        self.assertEqual(max, 5)
        max = max_integer([])
        self.assertEqual(max, None)

    def test_Two(self):
        """second test
        """
        with self.assertRaises(TypeError):
            max_integer(["x", 1, 2, 3])

if __name__ == '__main__':
    unittest.main()
