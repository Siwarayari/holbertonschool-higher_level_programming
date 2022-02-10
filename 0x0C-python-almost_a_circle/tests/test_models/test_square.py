#!/usr/bin/python3
"""Module for testing Square"""


import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square_Inst(unittest.TestCase):
    """Unittests for Square Class"""

    def test_base_parent(self):
        """Test for Base class as parent"""
        self.assertIsInstance(Square(1), Base)

    def test_two_arguments(self):
        """Test for two arguments"""
        square_1 = Square(1, 2)
        square_2 = Square(1, 2)
        self.assertEqual(square_1.id, square_2.id - 1)
