#!/usr/bin/python3
"""square unittest module"""
import io
import unittest
import os
import unittest.mock
from models.base import Base
from models.square import Square


class testSquareTwo(unittest.TestCase):
    """test basic initialization of square"""

    def testSquaret2(self):
        """testing basic initialization of Square objects"""
        r1 = Square(1, 0, 0, "r1")
        self.assertEqual(r1.id, "r1")
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.size, 1)
        self.assertRaises(TypeError, Square, "",  0, 0, "r2")
        self.assertRaises(TypeError, Square, None, 0, 0, "r2")
        self.assertRaises(TypeError, Square, "a", 0, 0, "r2")

        self.assertRaises(ValueError, Square, 0, 0, 0, "r2")
        self.assertRaises(ValueError, Square, -1, 0, 0, "r2")

        self.assertRaises(TypeError, Square, 2, "", 0, "r2")
        self.assertRaises(TypeError, Square, 2, None, 0, "r2")
        self.assertRaises(TypeError, Square, 2, "a", 0, "r2")
        self.assertRaises(ValueError, Square, 2, -2, 0, "r2")
        self.assertRaises(TypeError, Square, 2, 0, "", "r2")
        self.assertRaises(TypeError, Square, 2, 0, None, "r2")
        self.assertRaises(TypeError, Square, 2, 0, "b", "r2")
        self.assertRaises(ValueError, Square, 2, 0, -2, "r2")


class testArea(unittest.TestCase):
    """testing area method of square classs"""

    def testAreaCalc(self):
        """perform test to calculate area"""
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)
        r2 = Square(8,  0, 0, 122)
        self.assertEqual(r2.area(), 64)


class testDisplay(unittest.TestCase):
    """testing display of drawing square"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, rect, expected_output, mock_stdout):
        """initial setup for screen capture"""
        rect.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testPrintAreq(self):
        """test output and compare"""
        r1 = Square(3)
        self.assert_stdout(r1, "###\n###\n###\n")
        r2 = Square(2, 1, 1)
        self.assert_stdout(r2, "\n ##\n ##\n")
        r2 = Square(2, 2, 1)
        self.assert_stdout(r2, "\n  ##\n  ##\n")
        r2 = Square(5, 2, 3)
        self.assert_stdout(r2, "\n\n\n  #####\n  #####\n" +
                           "  #####\n  #####\n  #####\n")


class testStr(unittest.TestCase):
    """testing the string overload for square"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print(self, rect, expected_output, mock_stdout):
        """set up to capture the printed output"""
        print(rect)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testStrOverload(self):
        """test output and compare results"""
        r1 = Square(4, 2, 1, 12)
        self.assert_print(r1, "[Square] (12) 2/1 - 4\n")
        r2 = Square(1, 0, 0, "r3")
        self.assert_print(r2, "[Square] (r3) 0/0 - 1\n")
        r3 = Square(5, 1)
        self.assert_print(r3, "[Square] (%s) 1/0 - 5\n" % (r3.id))
        r3 = Square(2000000000000000000000000000000000000000000000, 1)
        self.assert_print(r3, "[Square] (%s) 1/0 - 200000000000000000\
0000000000000000000000000000\n" % (r3.id))


class testUpdate(unittest.TestCase):
    """testing the update method of square objects"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print(self, rect, expected_output, mock_stdout):
        """initial setup to get screen capture"""
        print(rect)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testUpdateVals(self):
        """test output and compare result"""
        r1 = Square(1, 1, 1)
        r1.update("r99")
        self.assert_print(r1, "[Square] (r99) 1/1 - 1\n")
        r1.update("r98", 2)
        self.assert_print(r1, "[Square] (r98) 1/1 - 2\n")
        r1.update("r97", 5)
        self.assert_print(r1, "[Square] (r97) 1/1 - 5\n")
        r1.update("r96", 4, 3)
        self.assert_print(r1, "[Square] (r96) 3/1 - 4\n")
        r1.update("r95", 5, 4, 9)
        self.assert_print(r1, "[Square] (r95) 4/9 - 5\n")
        r1.update("r95", 5, 4, 9, 9)
        self.assert_print(r1, "[Square] (r95) 4/9 - 5\n")
        r1.update("", 5, 4, 9)
        self.assert_print(r1, "[Square] (r95) 4/9 - 5\n")
        self.assertRaises(TypeError, r1.update, "r95", None, 3, 4)
        self.assertRaises(TypeError, r1.update, "r95", 1, None, 4)
        self.assertRaises(TypeError, r1.update, "r95", 1, 3, None)
        self.assertRaises(TypeError, r1.update, "r95", "", 3, 4)
        self.assertRaises(TypeError, r1.update, "r95", 1, "", 4)
        self.assertRaises(TypeError, r1.update, "r95", 1, 3, "")
        self.assertRaises(ValueError, r1.update, "r95", -1, 3, 4)
        self.assertRaises(ValueError, r1.update, "r95", 1, -1, 4)
        self.assertRaises(ValueError, r1.update, "r95", 1, 3, -1)

        r1.update("r94", id="r93")
        self.assert_print(r1, "[Square] (r94) 3/9 - 1\n")
        r1.update(id="r92")
        self.assert_print(r1, "[Square] (r92) 3/9 - 1\n")
        r1.update(size=5, x=5)
        self.assert_print(r1, "[Square] (r92) 5/9 - 5\n")
        r1.update(size=15, x=4)
        self.assert_print(r1, "[Square] (r92) 4/9 - 15\n")
        r1.update(id="r91", x=4, y=6, size=10)
        self.assert_print(r1, "[Square] (r91) 4/6 - 10\n")
        r1.update(id="r91", x=4, y=6, size=20, inval=1)
        self.assert_print(r1, "[Square] (r91) 4/6 - 20\n")
        r1.update(id="r91", nogood=5, x=4, y=6,
                  size=20, inval=1)
        self.assert_print(r1, "[Square] (r91) 4/6 - 20\n")
