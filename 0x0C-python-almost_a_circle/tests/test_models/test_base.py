#!/usr/bin/python3
"""The test module"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)


if __name__ == '__main__':
    unittest.main()
