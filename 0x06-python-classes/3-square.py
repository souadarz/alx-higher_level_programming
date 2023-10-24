#!/usr/bin/python3
"""Square class"""


class Square:
    """ define size of a square"""

    def __init__(self, size=0):
        """
        The __init__ method initializes the value of the size of a square
        args:
            size: the square size
        raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Define the area of a square"""

        return (self.__size ** 2)
