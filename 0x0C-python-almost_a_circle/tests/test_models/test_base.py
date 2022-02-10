#!/usr/bin/python3
"""Unitests for class base"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class Test_Base_Inst(unittest.TestCase):
    """Test for Instance of Base Class"""

    def test_pep8(self):
        """Test for Pep8"""
        pep8style_guide = pep8.StyleGuide()
        result = pep8style_guide.check_files(["models/base.py",
                                              "models/rectangle.py"])
        self.assertEqual(result.total_errors,
                         0,
                         'PEP8 style errors: %d' % result.total_errors)

    def test_no_arguments(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_module_docstr(self):
        """Test for module doc string"""
        base1 = Base()
        self.assertTrue(len(base1.__doc__) >= 1)

    def test_id(self):
        """Test id"""
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_id_change(self):
        """Set id"""
        base1 = Base(89)
        self.assertEqual(base1.id, 89)

    def test_to_json_string(self):
        """Tests to json string"""
        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(str,
                         type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test for None"""
        self.assertEqual('[]', Base.to_json_string(None))

    def test_from_json_string(self):
        """Test from json_string"""
        test_json = '[{"height": 7, "id": 1, "x": 2, "width": 10, "y": 8},\
                     {"height": 4, "id": 2, "x": 0, "width": 2, "y": 0}]'

        test_1 = Base.from_json_string(test_json)
        self.assertTrue(type(test_1) is list)
        self.assertTrue(type(test_1[0]) is dict)
