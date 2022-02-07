#!/usr/bin/python3
"""Rectangle Class"""


from models.base import Base


class Rectangle (Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """intialize instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, res):
        """width setter"""
        if type(res) is not int:
            raise TypeError("width must be an integer")
        elif res <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = res

    @height.setter
    def height(self, res):
        """height setter"""
        if type(res) is not int:
            raise TypeError("height must be an integer")
        elif res <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = res

    @x.setter
    def x(self, res):
        """x setter"""
        if type(res) is not int:
            raise TypeError("x must be an integer")
        elif res < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = res

    @y.setter
    def y(self, res):
        """y setter"""
        if type(res) is not int:
            raise TypeError("y must be an integer")
        elif res < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = res

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle"""
        for k in range(self.__y):
            print()
        for s in range(self.__height):
            for m in range(self.__x):
                print(" ", end='')
            for n in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """method so that it returns [Rectangle] (<id>) <x>/<y>"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    elif i == 'width':
                        self.__width = kwargs['width']
                    elif i == 'height':
                        self.__height = kwargs['height']
                    elif i == 'x':
                        self.__x = kwargs['x']
                    elif i == 'y':
                        self.__y = kwargs['y']

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height":
                self.height, "x": self.x, "y": self.y}
