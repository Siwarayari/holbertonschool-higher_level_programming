#!/usr/bin/python3
"""Test of Rectangle Class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rect_Inst(unittest.TestCase):
    """Test Rect Inst"""
    def test_rect_parent(self):
        """Test for Rect as Base"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_one_argument(self):
        """Test for one arg"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rect_basic(self):
        """Basic test of rectangle class"""
        rect_1 = Rectangle(1, 2)
        rect_2 = Rectangle(2, 1)
        self.assertEqual(rect_1.id, rect_2.id - 1)

    def test_rect_three_arguments(self):
        """Basic test of rectangle class"""
        rect_1 = Rectangle(1, 2, 3)
        rect_2 = Rectangle(2, 1, 3)
        self.assertEqual(rect_1.id, rect_2.id - 1)

    def test_rect_four_arguments(self):
        """Test four arguments"""
        rect_1 = Rectangle(1, 2, 3, 4)
        rect_2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_1.id, rect_2.id - 1)

    def test_rect_five_arguments(self):
        """Test Five arguments"""
        self.assertEqual(5, Rectangle(1, 2, 3, 4, 5).id)

    def test_rect_six_args(self):
        """Tests six arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_string_argument(self):
        """Test string arg"""
        with self.assertRaises(TypeError):
            Rectangle('Left', 4)

    def test_string_argument_2(self):
        """Test string arg"""
        with self.assertRaises(TypeError):
            Rectangle(4, 'Field')

    def test_string_argument_3(self):
        """Test string arg"""
        with self.assertRaises(TypeError):
            Rectangle(4, 5, 'Field')

    def test_string_argument_4(self):
        """Test string arg"""
        with self.assertRaises(TypeError):
            Rectangle(4, 5, 6, 'Field')

    def negative_parameter(self):
        """Negative Parameter"""
        Rectangle(-1, 2)
        raise ValueError
