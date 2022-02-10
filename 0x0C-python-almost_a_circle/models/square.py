#!/usr/bin/python3
"""Module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str() representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square"""
        arg_len = len(args)
        if arg_len != 0:
            if arg_len >= 1:
                self.id = args[0]
            if arg_len >= 2:
                self.size = args[1]
            if arg_len >= 3:
                self.x = args[2]
            if arg_len >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Create dictionary representation of Rect"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["size"] = self.size
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict
