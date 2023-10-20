#!/usr/bin/python3
"""The Rectangle test module"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_rectangle(self):
        rect1 = Rectangle(3, 4)
        self.assertEqual(rect1.width, 3)
        self.assertEqual(rect1.height, 4)

        rect2 = Rectangle(5, 4, 0, 0, 2)
        self.assertEqual(rect2.width, 5)
        self.assertEqual(rect2.height, 4)
        self.assertEqual(rect2.id, 2)

    def test_area(self):
        rect3 = Rectangle(5, 4)
        self.assertEqual(rect3.area(), 20)


if __name__ == '__main__':
    unittest.main()
