#!/usr/bin/python3
"""rectangle unittest module"""
import io
import unittest
import os
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle


class testRectangleTwo(unittest.TestCase):
    """testing rectangle class"""

    def testRectanglet2(self):
        """basic tests for rectangle class"""
        r1 = Rectangle(1, 2, 0, 0, "r1")
        self.assertEqual(r1.id, "r1")
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertRaises(TypeError, Rectangle, "", 1, 0, 0, "r2")
        self.assertRaises(TypeError, Rectangle, None, 1, 0, 0, "r2")
        self.assertRaises(TypeError, Rectangle, "a", 1, 0, 0, "r2")
        self.assertRaises(ValueError, Rectangle, 0, 1, 0, 0, "r2")
        self.assertRaises(ValueError, Rectangle, -1, 1, 0, 0, "r2")
        self.assertRaises(TypeError, Rectangle, 2, "", 0, 0, "r2")
        self.assertRaises(TypeError, Rectangle, 2, None, 0, 0, "r2")
        self.assertRaises(TypeError, Rectangle, 2, "a", 0, 0, "r2")
        self.assertRaises(ValueError, Rectangle, 2, 0, 0, 0, "r2")
        self.assertRaises(ValueError, Rectangle, 2, -1, 0, 0, "r2")
        self.assertRaises(TypeError, Rectangle, 2, 1, "", 0, "r2")
        self.assertRaises(TypeError, Rectangle, 2, 1, None, 0, "r2")
        self.assertRaises(TypeError, Rectangle, 2, 1, "a", 0, "r2")
        self.assertRaises(ValueError, Rectangle, 2, 1, -2, 0, "r2")
        self.assertRaises(TypeError, Rectangle, 2, 1, 0, "", "r2")
        self.assertRaises(TypeError, Rectangle, 2, 1, 0, None, "r2")
        self.assertRaises(TypeError, Rectangle, 2, 1, 0, "b", "r2")
        self.assertRaises(ValueError, Rectangle, 2, 1, 0, -2, "r2")


class testArea(unittest.TestCase):
    """testing the area method"""

    def testAreaCalc(self):
        """testing basic operations for area method"""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 5, 0, 0, 122)
        self.assertEqual(r2.area(), 40)


class testDisplay(unittest.TestCase):
    """testing displaying of data"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, rect, expected_output, mock_stdout):
        """test set up to capture screen"""
        rect.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testPrintAreq(self):
        """test compare screen output to expected output"""
        r1 = Rectangle(3, 2)
        self.assert_stdout(r1, "###\n###\n")
        r2 = Rectangle(2, 3, 1, 1)
        self.assert_stdout(r2, "\n ##\n ##\n ##\n")
        r2 = Rectangle(2, 3, 2, 1)
        self.assert_stdout(r2, "\n  ##\n  ##\n  ##\n")
        r2 = Rectangle(5, 3, 2, 3)
        self.assert_stdout(r2, "\n\n\n  #####\n  #####\n  #####\n")


class testStr(unittest.TestCase):
    """testing the str overload method"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print(self, rect, expected_output, mock_stdout):
        """set up the test to capture screen printout"""
        print(rect)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testStrOverload(self):
        """perform test and compare output"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assert_print(r1, "[Rectangle] (12) 2/1 - 4/6\n")
        r2 = Rectangle(1, 2, 0, 0, "r3")
        self.assert_print(r2, "[Rectangle] (r3) 0/0 - 1/2\n")
        r3 = Rectangle(5, 5, 1)
        self.assert_print(r3, "[Rectangle] (%s) 1/0 - 5/5\n" % (r3.id))
        r3 = Rectangle(150, 2000000000000000000000000000000000000000000000, 1)
        self.assert_print(r3, "[Rectangle] (%s) 1/0 - 150/200000000000000000\
0000000000000000000000000000\n" % (r3.id))


class testUpdate(unittest.TestCase):
    """testing update method of rectangle"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_print(self, rect, expected_output, mock_stdout):
        """initial setup of screen capture"""
        print(rect)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testUpdateVals(self):
        """perform test and compare"""
        r1 = Rectangle(1, 1, 1, 1)
        r1.update("r99")
        self.assert_print(r1, "[Rectangle] (r99) 1/1 - 1/1\n")
        r1.update("r98", 2)
        self.assert_print(r1, "[Rectangle] (r98) 1/1 - 2/1\n")
        r1.update("r97", 5, 3)
        self.assert_print(r1, "[Rectangle] (r97) 1/1 - 5/3\n")
        r1.update("r96", 4, 3, 2)
        self.assert_print(r1, "[Rectangle] (r96) 2/1 - 4/3\n")
        r1.update("r95", 5, 3, 4, 9)
        self.assert_print(r1, "[Rectangle] (r95) 4/9 - 5/3\n")
        r1.update("r95", 5, 3, 4, 9, 9)
        self.assert_print(r1, "[Rectangle] (r95) 4/9 - 5/3\n")
        r1.update("", 5, 3, 4, 9)
        self.assert_print(r1, "[Rectangle] (r95) 4/9 - 5/3\n")
        self.assertRaises(TypeError, r1.update, "r95", None, 3, 4, 9)
        self.assertRaises(TypeError, r1.update, "r95", 1, None, 4, 9)
        self.assertRaises(TypeError, r1.update, "r95", 1, 3, None, 9)
        self.assertRaises(TypeError, r1.update, "r95", 1, 3, 4, None)
        self.assertRaises(TypeError, r1.update, "r95", "", 3, 4, 9)
        self.assertRaises(TypeError, r1.update, "r95", 1, "", 4, 9)
        self.assertRaises(TypeError, r1.update, "r95", 1, 3, "", 9)
        self.assertRaises(TypeError, r1.update, "r95", 15, 30, 21, "")
        self.assertRaises(ValueError, r1.update, "r95", -1, 3, 4, 9)
        self.assertRaises(ValueError, r1.update, "r95", 1, -1, 4, 9)
        self.assertRaises(ValueError, r1.update, "r95", 1, 3, -1, 9)
        self.assertRaises(ValueError, r1.update, "r95", 15, 30, 21, -1)

        r1.update("r94", id="r93")
        self.assert_print(r1, "[Rectangle] (r94) 21/9 - 15/30\n")
        r1.update(id="r92")
        self.assert_print(r1, "[Rectangle] (r92) 21/9 - 15/30\n")
        r1.update(height=5, width=2)
        self.assert_print(r1, "[Rectangle] (r92) 21/9 - 2/5\n")
        r1.update(height=15, width=30, x=4)
        self.assert_print(r1, "[Rectangle] (r92) 4/9 - 30/15\n")
        r1.update(id="r91", x=4, y=6, height=10, width=20)
        self.assert_print(r1, "[Rectangle] (r91) 4/6 - 20/10\n")
        r1.update(id="r91", x=4, y=6, height=10, width=20, inval=1)
        self.assert_print(r1, "[Rectangle] (r91) 4/6 - 20/10\n")
        r1.update(id="r91", nogood=5, x=4, y=6, height=10,
                  width=20, inval=1)
        self.assert_print(r1, "[Rectangle] (r91) 4/6 - 20/10\n")
