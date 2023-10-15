#!/usr/bin/python3
"""The test module"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_base(self):
        b1 = Base()
        assertEqual(b1.id, 1)

        b2 = Base(10)
        assertEqual(b2.id, 10)
