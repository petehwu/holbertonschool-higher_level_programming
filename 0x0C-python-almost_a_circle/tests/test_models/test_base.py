#!/usr/bin/python3
"""base unittest module"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """first test case for base class"""

    def test_this(self):
        """testing initialization"""
        b1 = Base()
        self.assertEqual(b1.id, Base._Base__nb_objects)
        b2 = Base("hi")
        self.assertEqual(b2.id, "hi")
        b3 = Base([1])
        self.assertEqual(b3.id, [1])
        b4 = Base({1: 1})
        self.assertEqual(b4.id, {1: 1})
        b5 = Base((2, 2))
        self.assertEqual(b5.id, (2, 2))
        b6 = Base()
        self.assertEqual(b6.id, Base._Base__nb_objects)
        b7 = Base()
        self.assertEqual(b7.id, Base._Base__nb_objects)
        b8 = Base(["x"])
        self.assertEqual(b8.id, ["x"])
        b9 = Base([])
        self.assertEqual(b9.id, [])
        b10 = Base({})
        self.assertEqual(b10.id, {})
        b11 = Base()
        self.assertEqual(Base._Base__nb_objects, b11.id)


class TestDictToJson(unittest.TestCase):
    """test dictionary to json"""

    def testDict(self):
        """test serialize to json"""
        l1 = [{"k1": "v1", "k2": "v2", "k3": "v3"},
              {"kk1": "vv1", "kk2": "vv2", "kk3": "vv3"}]
        json_dictionary = Base.to_json_string(l1)
        self.assertIs(type(json_dictionary), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertIs(type(Base.to_json_string([])), str)
        self.assertEqual(Base.to_json_string(["blah", "foo"]),
                         '["blah", "foo"]')
        l1 = [{"k1": {"kk1": "vv1", "kk1": "vv2"},
              "k2": "v2"}, {"c1": "vv1", "c2": "vv2"}]
        json_dictionary = Base.to_json_string(l1)
        self.assertIs(type(json_dictionary), str)


class TestSaveToFile(unittest.TestCase):
    """test save to file"""

    def testSave(self):
        """test save to file method"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 5, 0, 0)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.access("Rectangle.json", os.F_OK))
        self.assertNotEqual(os.path.getsize("Rectangle.json"), 2)
        Rectangle.save_to_file(None)
        self.assertEqual(os.path.getsize("Rectangle.json"), 2)

        s1 = Square(2, 0, 0, 1)
        s2 = Square(3, 0, 0, 2)
        s3 = Square(5, 0, 0, 3)
        Square.save_to_file([s1, s2, s3])
        self.assertTrue(os.access("Square.json", os.F_OK))
        self.assertNotEqual(os.path.getsize("Square.json"), 2)
        Square.save_to_file(None)
        self.assertEqual(os.path.getsize("Square.json"), 2)


class testFromJsonString(unittest.TestCase):
    """test deserilzie from json to string"""

    def testJsonToString(self):
        """test change from json to string"""
        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(Rectangle.from_json_string(None), [])
        s1 = '[{"k1": "v1","k2": "v2"},{"k3": "v3", "k4": "v4"}]'
        self.assertIs(type(Rectangle.from_json_string(s1)), list)
        l1 = Rectangle.from_json_string('[{"k1": "v1", "k2": "v2"}]')
        for d in l1:
            self.assertDictEqual(d, {"k1": "v1", "k2": "v2"})


class testCreate(unittest.TestCase):
    """test create object from json"""

    def testCreatedict(self):
        """test create a dictionary"""
        r1 = Rectangle(3, 5, 1, 1, "r1")
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        self.assertEqual(r2.id, "r1")
        self.assertRaises(TypeError, Rectangle.create, **{})
        self.assertRaises(TypeError, Rectangle.create, None)
        s1 = Square(3, 1, 1, "s1")
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)
        self.assertEqual(s2.id, "s1")
        r1 = Rectangle(3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        self.assertEqual(r2.id, r1.id)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)
        self.assertEqual(s2.id, s1.id)
        self.assertEqual(s2.x, s1.x)
        self.assertEqual(s2.y, s1.y)
        self.assertEqual(s1.size, s2.size)


class testLoadFile(unittest.TestCase):
    """testing save to file"""

    def testLoadFromFile(self):
        """test loading object from file"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        li = Rectangle.load_from_file()
        self.assertListEqual(li, [])
        li = Square.load_from_file()
        self.assertListEqual(li, [])
        r1 = Rectangle(10, 5, 3, 2, "r1")
        lri = [r1]
        Rectangle.save_to_file(lri)
        lro = Rectangle.load_from_file()
        for obj in lro:
            self.assertEqual(obj.width, 10)
            self.assertNotEqual(id(obj), id(r1))
        lro2 = Rectangle.load_from_file()
        for obj2 in lro2:
            self.assertEqual(obj2.width, 10)
            self.assertEqual(obj2.height, 5)
            self.assertNotEqual(id(obj), id(obj2))
            self.assertNotEqual(id(obj2), id(r1))
        s1 = Square(8, 0, 0, "s1")
        lsi = [s1]
        Square.save_to_file(lsi)
        lso = Square.load_from_file()
        for obj in lso:
            self.assertEqual(obj.size, 8)
            self.assertNotEqual(id(obj), id(s1))
        lso2 = Square.load_from_file()
        for obj2 in lso2:
            self.assertEqual(obj2.size, 8)
            self.assertNotEqual(id(obj), id(obj2))
            self.assertNotEqual(id(obj2), id(s1))
