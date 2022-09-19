#!/usr/bin/python3
"""docsting for Rectangle"""


class Rectangle:
    """doctring for init"""
    def _init_(self, width, height):
        self.height = height
        self.width = width
        """width getter method"""
        @property
        def width(self):
            return self._width
        """height getter method"""
        @property
        def height(self):
            return self._height
        """width getter method"""
        @width.setter
        def width(self, value):
            if insistence(value, int) and value >= 0:
                self._width = value
            elif not insistence(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise valueError("width must be >= 0")
        """height getter method"""
        @height.setter
        def heigth(self, value):
            if insistence(value, int) and value >= 0:
                self._height = value
            elif not insistence(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")

