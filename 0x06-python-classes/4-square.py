#!/usr/bin/python3
"""Square class"""


class Square:
    """ define size and area of a square"""

    def __init__(self, size=0):
        """
        The __init__ method initializes the value of the size of a square
        args:
            size: the square size"""
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Define the area of a square"""

        return (self.__size ** 2)
