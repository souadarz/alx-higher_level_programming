#!/usr/bin/python3
"""Square class"""


class Square:
    """ define size and area of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method initializes the value of the size of a square
        args:
            size: the square size
            position: the square position
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrive the position of a square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Define the area of a square"""

        return (self.__size ** 2)

    def my_print(self):
        """prints the square with the character #"""

        if self.__size > 0:
            for i in range(self.position[1]):
                print("")
            for i in range(0, self.__size):
                for n in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
